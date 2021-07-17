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
    title_name = story.title_name
    created_time = story.created_time
    category = story.category
    views = story.views
    text = story.text
    video = story.video
    paper_link = story.paper_link
    try:
        video = f"https://www.youtube.com/embed/{video.split('/')[-1]}"
    except AttributeError:
        pass
    kwarg = {
        "title_name": title_name,
        "created_time": created_time,
        "category": category,
        "views": views,
        "text": text,
        "video": video,
        "paper_link": paper_link
    }

    story.viewed()

    return render(request, 'storyPage.html', kwarg)




