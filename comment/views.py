from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from Story.models import Story
from comment.forms import CommentForm
from comment.models import Comment


@login_required
def post_comment(request, story_id):
    story = get_object_or_404(Story, id=story_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.story = story
            new_comment.user = request.user

            new_comment.save()
            # redirect()：返回到一个适当的url中：即用户发送评论后，重新定向到文章详情页面。
            # 当其参数是一个Model对象时，会自动调用这个Model对象的get_absolute_url()方法。
            # return HttpResponseRedirect(reverse("Story:getStory", args=[story.id]))
            return redirect(story)
        else:
            return HttpResponse('There is something wrong with this form. Please fill it out again. ')
    else:
        comment_form = CommentForm()
        context = {'comment_form': comment_form,
                   'story_id': story_id,
                   'story': story,
                   }
        # return render(request, 'detail.html', context)
        return HttpResponse('Only POST requests are accepted for Posting comments. ')
