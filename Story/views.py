from django.shortcuts import render
from .models import Story


def storyList(request):
    story = Story.objects.filter()
    return render(request, 'story.html', locals())


def storyListCategory(request, category):
    story = Story.objects.filter(category=category)
    return render(request, 'story.html', locals())


def getStory(request, story_id):
    story = Story.objects.filter(id=story_id)
    return render(request, 'story.html', locals())


"""

127.0.0.1/story/id

"""

