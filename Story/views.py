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



def upload(request):
    if request.method == "GET":
        form = StoryForm()
    elif request.method == "POST":
        form = StoryForm(data=request.POST)
        if form.is_valid():
            story = Story()
            story.title_name = request.POST.get('title')
            story.category = request.POST.get('category')
            story.text = request.POST.get('text')
            story.video = request.POST.get('videoUrl')
            story.paper_link = request.POST.get('paperLink')
            story.img = request.POST.get('img')
            story.save()
            return HttpResponseRedirect(reverse("Story:storyList"))
    return render(request, 'upload.html', locals())


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
        return render(request, 'search/advancedSearchPage.html', locals())
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

        que = Q()
        for word in keyword.split():
            que &= Q(title_name__icontains=word)
        if keyword_negate == "on":
            que = ~que

        if category != "All":
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
    text = re.sub(r'&rdquo;', '\"', text)
    text = re.sub(r'&ldquo;', '\"', text)

    video = story.video
    paper_link = story.paper_link

    comments = Comment.objects.filter(story=story_id)
    comment_form = CommentForm()


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
    }

    story.viewed()
    return render(request, 'storyPage.html', kwarg)
