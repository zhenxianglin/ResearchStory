from django.shortcuts import render
from datetime import datetime
from meeting.models import Link
from meeting.meetingforms import MeetingForm
from Users.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


def time_in_mins(hr, min):
    return hr * 60 + min


def current_meeting(request):
    current_time = datetime.now()
    current_hour = current_time.hour
    current_min = current_time.minute
    meeting_list = list(Link.objects.all().order_by('-data_added'))
    current_meetings = []
    for meeting in meeting_list:
        start_time_hour = meeting.start_time.hour
        start_time_min = meeting.start_time.minute
        end_time_hour = meeting.end_time.hour
        end_time_min = meeting.end_time.minute
        day_list = []
        if meeting.monday == True:
            day_list.append('Monday')
        if meeting.tuesday == True:
            day_list.append('Tuesday')
        if meeting.wednesday == True:
            day_list.append('Wednesday')
        if meeting.thursday == True:
            day_list.append('Thursday')
        if meeting.friday == True:
            day_list.append('Friday')
        if meeting.saturday == True:
            day_list.append('Saturday')
        if meeting.sunday == True:
            day_list.append('Sunday')
        if ((day_list.count(current_time.strftime('%A')) != 0)
                and (time_in_mins(end_time_hour, end_time_min)) > time_in_mins(current_hour, current_min)):
            # continue
            current_meetings.append(meeting)
    date_and_time = current_time.strftime("%Y-%m-%d, %A,  %H:%M:%S")

    if len(current_meetings) == 0:
        context = {'date_and_time': date_and_time}
        return render(request, 'meeting/nomeetings.html', context)
    else:
        context = {
            'current_meetings': current_meetings,
            'date_and_time': date_and_time,
                   }
        return render(request, 'meeting/linktoclick.html', context)

    # current_meetings = Link.objects.all().order_by('-data_added')
    # # context = {"current_meetings":current_meetings}
    # # return render(request, 'meeting/linktoclick.html', context)


def new_meeting(request):
    """add a new meeting for discussion freely"""
    current_time = datetime.now()
    date_and_time = current_time.strftime("%Y-%m-%d, %A,  %H:%M:%S")

    if request.method != 'POST':
        form = MeetingForm()
    else:
        form = MeetingForm(data=request.POST)
        if form.is_valid():
            new_meeting = form.save(commit=False)
            new_meeting.user = request.user
            new_meeting.save()
            return HttpResponseRedirect(reverse('meeting:current_meeting'))
    context = {
        'form': form,
        'date_and_time':date_and_time,
    }
    return render(request, 'meeting/new_meeting.html', context)
