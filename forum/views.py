from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from forum.models import Forum, ForumComment
from forum.ForumForm import ForumForm,CommentForm


def forumList(request):
    if request.method == "GET":
        form = ForumForm()
        forum = Forum.objects.filter().order_by('created_time')
        kwargs = {"forum": forum,
                  "form": form,
                  }
        return render(request, 'forum/forum_list.html', kwargs)
    elif request.method == "POST":
        form = ForumForm(data=request.POST)
        # if form.is_valid():
        forum = Forum()
        mistake = False
        kwargs = {}
        if request.POST.get('title'):
            print("title: ", request.POST.get('title'))
            forum.title = request.POST.get('title')
        else:
            kwargs["title"] = "You must write title name."
            mistake = True
        # forum.title=request.POST.get('title')
        forum.author = request.user
        # forum.created_time=request.POST.get('created_time')
        forum.text = request.POST.get('text')
        if not mistake:
            forum.save()
            return HttpResponseRedirect(reverse("forum:forumList"))
        else:
            return render(request, "Fail/upload_fail.html", kwargs)
    # return render(request, 'forum/forum_list.html', locals())


@login_required
def post_forum(request, forum_id, parent_forumcomment_id=None):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        # if forum.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.forum = forum
        new_comment.user = request.user
        #print('!!!!!',new_comment)
        # second
        if parent_forumcomment_id:
            parent_comment = ForumComment.objects.get(id=parent_forumcomment_id)
            # 如果层级超过二级，则自动转为二级
            new_comment.parent_id = parent_comment.get_root().id
            # 被回复人
            new_comment.reply_to = parent_comment.user
            new_comment.save()
            return HttpResponse("200 OK")
        new_comment.save()
        return redirect(forum)


    elif request.method == 'GET':
        comment_form = CommentForm()
        # forum = Forum.objects.get(id=parent_forumcomment_id)
        kwargs = {"comment_form": comment_form,
                  "forum_id": forum_id,
                  "forum": forum,
                  "parent_forumcomment_id": parent_forumcomment_id,
                  }
        return render(request, 'forum/forum_reply.html', kwargs)


def get_forum(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    title = forum.title
    author = forum.author
    created_time = forum.created_time
    text = forum.text
    views = forum.views

    comments = ForumComment.objects.filter(forum=forum_id)
    comment_form = CommentForm()

    context = {"forum": forum,
               "title": title,
               "author": author,
               "created_time": created_time,
               "text": text,
               "views": views,
               "comments": comments,
               "comment_form": comment_form,
               }
    forum.viewed()
    return render(request, 'forum/forum_page.html', context)
