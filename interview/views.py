from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from interview.forms import InterviewForm
from datetime import datetime
from Story.models import Story
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


# @login_required
def new_interview(request, story_id):
    """book a new interview """
    story = Story.objects.get(id=story_id)
    current_time = datetime.now()
    date_and_time = current_time.strftime("%Y-%m-%d, %A,  %H:%M:%S")

    if request.method != 'POST':
        form = InterviewForm()
    else:
        form = InterviewForm(data=request.POST)
        if form.is_valid():
            new_interview = form.save(commit=False)
            new_interview.related_story_name = story
            new_interview.organizer = request.user
            new_interview.save()
            return HttpResponseRedirect(reverse('Story:getStory', args=[story_id]))

    context = {'story': story,
               'form': form,
               'date_and_time': date_and_time
               }
    return render(request, 'interview/new_interview.html', context)
