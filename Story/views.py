from django.shortcuts import render
from .models import Story
from .storyform import StoryForm, AdvancedSearchForm

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from comment.models import Comment
from comment.forms import CommentForm
import re
from interview.models import Interview
from datetime import datetime
import os
from django.contrib import messages

from ResearchStory.settings import MEDIA_ROOT

def edit(request,story_id):
    story=Story.objects.get(id=story_id)
    if request.method == "GET":
         form = StoryForm(instance=story)
         '''kwargs={"form":form,
                 # "story":story,
         }
         return render(request, 'edit.html', kwargs)'''
    elif request.method == "POST":
        form = StoryForm(instance=story,data=request.POST)
        #if form.is_valid():
        story.title_name = request.POST.get('title')
        story.category = request.POST.get('category')
        story.text = request.POST.get('text')
        story.video = request.POST.get('videoUrl')
        story.paper_link = request.POST.get('paperLink')
        f = request.FILES['img']
        filepath = os.path.join(MEDIA_ROOT, 'img/' + f.name)
        with open(filepath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)  # chunks是以文件流的方式来接受文件，分段写入
        story.img = 'img/' + f.name
        story.author = request.POST.get('author')
        story.author_intro = request.POST.get('author_intro')
        story.background = request.POST.get('background')
        story.tags = request.POST.get('tags')
        story.user = request.user
        story.save()
        return HttpResponseRedirect(reverse("Story:getStory",args=[story_id]))

        # if form.is_valid():
        #     return HttpResponseRedirect(reverse("Story:getStory"))

    return render(request, 'edit.html', locals())


def upload(request):
    if request.method == "GET":
        form = StoryForm()
        return render(request, 'upload.html', locals())
    elif request.method == "POST":
        kwargs = {}
        form = StoryForm(data=request.POST)
        story = Story()
        mistake = False

        if request.POST.get('title'):
            print("title: ", request.POST.get('title'))
            story.title_name = request.POST.get('title')
        else:
            kwargs["title"] = "You must write title name."
            mistake = True

        if request.POST.get('category'):
            print("category: ", request.POST.get('category'))
            story.category = request.POST.get('category')
        else:
            kwargs["category"] = "You must choose a category."
            mistake = True

        if request.POST.get('text'):
            print("text: ", request.POST.get('text'))
            story.text = request.POST.get('text')
        else:
            kwargs["text"] = "You must write something in text form."
            mistake = True

        if request.POST.get('background'):
            print("background: ", request.POST.get('background'))
            story.background = request.POST.get('background')
        else:
            kwargs["background"] = "You must provide a reseach background."
            mistake = True

        if request.POST.get('author'):
            print("Author: ", request.POST.get('author'))
            story.author = request.POST.get('author')
        else:
            user = request.POST.get('user')
            story.author = user.username
            print("Author: ", user.username)

        if request.POST.get("author_intro"):
            print("author_intro: ", request.POST.get("author_intro"))
            story.author_intro = request.POST.get('author_intro')
        else:
            story.author_intro = "This author does not introduce himself/herself."
            print("Author_intro: ", story.author_intro )

        if request.FILES.get('img'):
            f = request.FILES['img']
            filepath = os.path.join(MEDIA_ROOT, 'img/' + f.name)
            with open(filepath, 'wb') as fp:
                for info in f.chunks():
                    fp.write(info)  # chunks是以文件流的方式来接受文件，分段写入
            print('filepath:', filepath)
            print("img: ", request.FILES.get('img'))
            story.img = 'img/' + f.name
        else:
            story.img = "default.png"
            print(story.img)

        print("tag: ", request.POST.get('tags'))
        story.tags = request.POST.get('tags')

        print("video: ", request.POST.get("videoUrl"))
        story.video = request.POST.get('videoUrl')

        print("paper_link: ", request.POST.get("paper_link"))
        story.paper_link = request.POST.get('paperLink')

        story.user = request.user
        # story.img = 'img/'+request.POST.get('img')
        # print(request.FILES['file'])

        if not mistake:
            story.save()
            return HttpResponseRedirect(reverse("Story:storyList"))
        else:
            return render(request, "Fail/upload_fail.html", kwargs)


def delete(request, story_id):
    story = Story.objects.filter(id=story_id)
    if story:
        story.delete()
    return HttpResponseRedirect(reverse("Story:storyList"))


def search(request):
    if request.method == "POST":
        keyword = request.POST.get("keyword")

        que = Q()
        for word in keyword.split():
            que &= Q(title_name__icontains=word)

        story = Story.objects.filter(que)
        kwargs = {
            "story": story,
        }
        return render(request, 'story.html', kwargs)


def advancedSearch(request):
    if request.method == "GET":
        form = AdvancedSearchForm()
        return render(request, 'advancedSearchPage.html', locals())
    elif request.method == "POST":
        keyword = request.POST.get("keyword")
        keyword_negate = request.POST.get("keyword_negate")

        operator1 = request.POST.get("operator1")
        category_negate = request.POST.get("category_negate")

        category = request.POST.get("category")

        operator2 = request.POST.get("operator2")

        start_at = request.POST.get("start_at")
        end_at = request.POST.get("end_at")
        time_negate = request.POST.get("time_negate")
        sort = request.POST.get("sort")

        que = Q()
        if keyword!='':
            for word in keyword.split():
                que &= Q(title_name__icontains=word)
            if keyword_negate == "on":
                que = ~que

        if category != "ALL":
            if operator1 == "AND":
                que &= Q(category=category)
            else:
                que |= Q(category=category)
        if category_negate == "on":
            que = ~que

        if operator2 == "AND":
            que &= Q(created_time__range=(start_at, end_at))
        else:
            que |= Q(created_time__range=(start_at, end_at))
        if time_negate == "on":
            que = ~que

        story = Story.objects.filter(que)
        if (sort == "hot"):
            story = story.order_by("-views")
        kwargs = {
            "story": story,
        }

        return render(request, 'story.html', kwargs)


def storyList(request):
    if request.method == "GET":
        story = Story.objects.filter().order_by('-created_time')
        kwarg = {
            "story": story,
        }
        return render(request, 'story.html', kwarg)
    elif request.method == "POST":
        method = request.POST.get("sort_by")
        story = request.POST.get("story")
        if method == "time":
            story.order_by("-created_time")
        elif method == "hot":
            story.order_by("-views")
        kwarg = {
            "story": story,
        }
        return render(request, 'story.html', kwarg)


def storyListSortBy(request, sort_by):
    story = Story.objects.filter()
    if sort_by == "time":
        story = story.order_by("-created_time")
    elif sort_by == "hot":
        story = story.order_by("-views")
    print(story)
    kwarg = {
        "story": story,
    }
    return render(request, 'story.html', kwarg)


def storyListCategory(request, category):
    print("storyListCategory")
    print("method =", request.method)
    if request.method == "GET":
        story = Story.objects.filter(category=category).order_by('-created_time')
        kwarg = {
            "story": story,
        }
        return render(request, 'story.html', kwarg)
    elif request.method == "POST":
        method = request.POST.get("sort_by")
        story = request.POST.get("story")
        if method == "time":
            story.order_by("-created_time")
        elif method == "hot":
            story.order_by("-views")
        kwarg = {
            "story": story,
        }
        return render(request, 'story.html', kwarg)


def storyListCategorySortBy(request, category, sort_by):
    story = Story.objects.filter(category=category)
    if sort_by == "time":
        story = story.order_by("-created_time")
    elif sort_by == "hot":
        story = story.order_by("-views")
    print(story)
    kwarg = {
        "story": story,
    }
    return render(request, 'story.html', kwarg)


def storyFind(request, category, sort_by, title):
    que = Q()
    if title != '_all':
        for word in title.split():
            que &= Q(title_name__icontains=word)

    if category != "ALL":
        que &= Q(category=category)

    story = Story.objects.filter(que)
    if sort_by == "time":
        story = story.order_by("-created_time")
    elif sort_by == "hot":
        story = story.order_by("-views")

    kwarg = {
        "story": story,
    }
    return render(request, 'story.html', kwarg)


def time_in_mins(hr, min):
    return hr * 60 + min


def getStory(request, story_id):
    story = Story.objects.get(id=story_id)
    title_name = story.title_name
    created_time = story.created_time
    category = story.category
    views = story.views

    img = story.img

    text = story.text
    text = re.sub(r'\<.*?\>', '', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&rsquo;', '\'', text)
    text = re.sub(r'&lsquo;', '\'', text)
    text = re.sub(r'&rdquo;', '\"', text)
    text = re.sub(r'&ldquo;', '\"', text)
    text = re.sub(r'&#39;', '\'', text)
    text = re.sub(r'&mdash;', '-', text)
    text = re.sub(r'&quot;', '\"', text)

    video = story.video
    paper_link = story.paper_link

    comments = Comment.objects.filter(story=story_id)
    comment_form = CommentForm()

    tags = story.tags
    author = story.author
    author_intro = story.author_intro
    background = story.background


    try:
        video = f"https://www.youtube.com/embed/{video.split('/')[-1]}"
    except AttributeError:
        pass

    interview_list = Interview.objects.filter(related_story_name = story_id)
    current_time = datetime.now()
    date_and_time = current_time.strftime("%Y-%m-%d, %A,  %H:%M:%S")
    current_hour = current_time.hour  # 3:00 pm -> 15
    current_min = current_time.minute  # 3:00 pm -> 0
    # interview_list = list(Interview.objects.filter(related_story_name=story_id))
    current_interview = None
    for interview in interview_list:
        start_time_hour = interview.start_time.hour
        start_time_min = interview.start_time.minute
        end_time_hour = interview.end_time.hour
        end_time_min = interview.end_time.minute
        day_list = []
        if interview.monday == True:
            day_list.append('Monday')
        if interview.tuesday == True:
            day_list.append('Tuesday')
        if interview.wednesday == True:
            day_list.append('Wednesday')
        if interview.thursday == True:
            day_list.append('Thursday')
        if interview.friday == True:
            day_list.append('Friday')
        if ((day_list.count(current_time.strftime('%A')) == 0)
                or (time_in_mins(end_time_hour, end_time_min)) < time_in_mins(current_hour, current_min)):
            continue
        current_interview = interview


    kwarg = {
        "img": img,
        "title_name": title_name,
        "created_time": created_time,
        "category": category,
        "views": views,
        "text": text,
        "video": video,
        "paper_link": paper_link,

        'comments': comments,
        'comment_form': comment_form,
        'story': story,

        'data_and_time':date_and_time,
        'current_intervew':current_interview,

        'tags': tags,
        'author': author,
        'author_intro': author_intro,
        'background': background,
    }

    story.viewed()
    return render(request, 'storyPage.html', kwarg)
