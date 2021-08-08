from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from comment.models import Comment
from comment.forms import CommentForm
from Story.models import Story

from Users.models import User
from django.views import View


@login_required
def post_comment(request, story_id, parent_comment_id=None):
    """ publish a new comment and reply a comment. """
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.story = story
            new_comment.user = request.user
            # second level comment
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                new_comment.parent_id = parent_comment.get_root().id
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse("200 OK")

            new_comment.save()
            return redirect(story)
        else:
            return render(request,'Fail/comments_fail.html')

            # return HttpResponse('There is something wrong with this form. Please fill it out again. ')
    # GET request
    else:
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'story_id': story_id,
            'story': story,
            'parent_comment_id': parent_comment_id,
        }
        return render(request, 'comment/reply.html', context)
