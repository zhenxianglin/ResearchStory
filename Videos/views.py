from django.shortcuts import render
from Videos.models import Video

def video_list(request):
    videos = Video.objects.all()
    context = {'videos':videos}
    return render(request, 'Videos/video_list.html',context)