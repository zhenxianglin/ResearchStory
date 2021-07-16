from django.shortcuts import render
from .models import Story


def storyList(request):
    story = Story.objects.filter()
    return render(request, 'story.html', locals())


def storyListCategory(request, category):
    story = Story.objects.filter(category=category)
    return render(request, 'story.html', locals())


def getStory(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'story.html', locals())



