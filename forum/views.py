from django.shortcuts import render
from forum.models import Forum



def forumList(request):
    if request.method == "GET":
        forum = Forum.objects.filter().order_by('created_time')
        return render(request, 'forum_list.html', locals())

def post_new_thread(request,parent_comm_id=None):
    if request.method == 'POST':
        comment_form = ForumForm(request.POST)
