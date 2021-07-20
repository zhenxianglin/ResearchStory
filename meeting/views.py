from django.shortcuts import render
from datetime import datetime
from meeting.models import Link

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


def current_meeting(request):

    current_meetings = Link.objects.all().order_by('-data_added')

    context = {"current_meetings":current_meetings}

    return render(request, 'meeting/linktoclick.html', context)
    #
    # current_time = datetime.now()
    #
    # current_hour = current_time.hour
    # current_min = current_time.minute
    #
    # meeting_list = list(Link.objects.all())
    #
    # current_meetings = None
    #
    # def time_in_mins(hr, min):
    #     return hr * 60 + min
    #
    # for meeting in meeting_list:
    #     start_time_hour = meeting.start_time.hour
    #     start_time_min = meeting.start_time.minute
    #
    #     end_time_hour = meeting.end_time.hour
    #     end_time_min = meeting.end_time.minute
    #
    #     day_list = []
    #     if meeting.monday == True:
    #         day_list.append('Monday')
    #     if meeting.tuesday == True:
    #         day_list.append('Tuesday')
    #     if meeting.wednesday == True:
    #         day_list.append('Wednesday')
    #     if meeting.thursday == True:
    #         day_list.append('Thursday')
    #     if meeting.friday == True:
    #         day_list.append('Friday')
    #     if meeting.saturday == True:
    #         day_list.append('Saturday')
    #     if meeting.sunday == True:
    #         day_list.append('Sunday')
    #
    #     if ((day_list.count(current_time.strftime('%A')) == 0)
    #             or (time_in_mins(start_time_hour, start_time_min) - 6) > time_in_mins(current_hour, current_min)
    #             or (time_in_mins(end_time_hour, end_time_min)) < time_in_mins(current_hour, current_min)):
    #         continue
    #     current_meetings = meeting
    #
    # if current_meetings == None:
    #     return render(request, 'meeting/nomeetings.html')
    #
    # else:
    #     return render(request, 'meeting/linktoclick.html', {'current_meetings': current_meetings})
#
#