from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from forum.models import Forum
from forum.ForumForm import ForumForm

def forumList(request):
    if request.method == "GET":
        form = ForumForm()
        forum = Forum.objects.filter().order_by('created_time')
        kwargs = {"forum": forum,
                  "form": form,
                  }
        return render(request, 'forum/forum_list.html', kwargs)
    elif request.method=="POST":
        form=ForumForm(data=request.POST)
        if form.is_valid():
            forum=Forum()
            forum.title=request.POST.get('title')
            #forum.author=request.POST.get('author')
            #forum.created_time=request.POST.get('created_time')
            forum.text=request.POST.get('text')
            forum.save()
            return HttpResponseRedirect(reverse("forum:forumList"))
    return render(request, 'forum/forum_list.html', locals())



def post_forum(request,parent_forum_id):
    if request.method == 'POST':
        forum = ForumForm(request.POST)

        if forum.is_valid():
            new_forum = forum.save(commit=False)
            new_forum.author = request.author

            # second
            if parent_forum_id:
                parent_forum = Forum.objects.get(id=parent_forum_id)
                # 如果层级超过二级，则自动转为二级
                new_forum.parent_id = parent_forum.get_root().id
                # 被回复人
                new_forum.reply_to = parent_forum.author
                new_forum.save()
                return HttpResponse("200 OK")
            new_forum.save()
            return HttpResponseRedirect(reverse("forum:forumList"))  # redirect(story)

        else:
            return HttpResponse('There is something wrong with this form. Please fill it out again. ')

    elif request.method == 'GET':
        forum = ForumForm()
        kwargs = {"forum": forum}
        return render(request, 'forum/forum_reply.html', kwargs)