from django.shortcuts import render
from .models import Story
from .storyform import StoryForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from comment.models import Comment
from comment.forms import CommentForm


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


def storyList(request):
    print("method =", request.method)
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


def getStory(request, story_id):
    story = Story.objects.get(id=story_id)
    title_name = story.title_name
    created_time = story.created_time
    category = story.category
    views = story.views
    text = story.text
    video = story.video
    paper_link = story.paper_link

    comments = Comment.objects.filter(story=story_id)

    try:
        video = f"https://www.youtube.com/embed/{video.split('/')[-1]}"
    except AttributeError:
        pass

    comment_form = CommentForm()

    kwarg = {
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
    }

    story.viewed()

    return render(request, 'storyPage.html', kwarg)
