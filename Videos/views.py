from django.shortcuts import render
from Videos.models import Video, Classification, VideoComment
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from Videos.forms import VideoCommentForm, NewVideoForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class VideoIndexView(generic.ListView):
    model = Video
    template_name = 'Videos/video_list.html'
    context_object_name = 'videos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VideoIndexView, self).get_context_data(**kwargs)
        classification_list = Classification.objects.filter(status=True).values()

        context['classification_list'] = classification_list
        return context

    def get_queryset(self):
        self.c = self.request.GET.get("c", None)
        if self.c:
            classification = get_object_or_404(Classification, pk=self.c)
            return classification.video_set.all().order_by("-created_time")
        else:
            return Video.objects.filter().order_by('-created_time')


def video_detail(request, video_id):
    """showing a video deatail on a single page"""
    video = get_object_or_404(Video, id=video_id)
    video_comments = VideoComment.objects.filter(video=video_id)
    video_comment_form = VideoCommentForm()

    context = {'video': video,
               'video_comments': video_comments,
               'video_comment_form': video_comment_form,
               }
    return render(request, 'Videos/video_detail.html', context)


@login_required
def post_video_comment(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video_comment_form = VideoCommentForm(data=request.POST)
        if video_comment_form.is_valid():
            new_comment = video_comment_form.save(commit=False)
            new_comment.video = video
            new_comment.user = request.user
            new_comment.save()

            return redirect(video)
        else:
            return HttpResponse("The content of the form is incorrect, please fill in again. ")
    else:
        return HttpResponse("Only POST requests are accepted for comments.")


@login_required
def new_video(request):
    """add a new interview video"""
    classification = Classification.objects.all().values()
    if request.method != 'POST':
        form = NewVideoForm()
    else:
        form = NewVideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.uploader = request.user
            new_form.save()
            return HttpResponseRedirect(reverse("Videos:video_list"))
    context = {"form": form,
               'classification': classification,
               }
    return render(request, 'Videos/new_video.html', context)


@login_required
def edit_video(request, video_id):
    video = Video.objects.get(id=video_id)
    classification = Classification.objects.all().values()
    #  Protect page
    if video.uploader != request.user:
        raise Http404
    if request.method == "POST":
        form = NewVideoForm(instance=video, data=request.POST, files=request.FILES)
        if form.is_valid():
            video.title = request.POST['title']
            video.desc = request.POST['desc']
            video.url = request.POST['url']

            if 'file' in request.FILES:
                video.file = request.POST['files']

            video.save()
            # return HttpResponse("edit successful")
            return HttpResponseRedirect(reverse("Videos:video_detail", args=[video_id]))
        else:
            return HttpResponse("<h1>The content of the form is incorrect, please fill in again.</h1>")
    else:
        form = NewVideoForm(instance=video)
        context = {'video': video, 'classification': classification, 'form': form}
        return render(request, "Videos/edit_video.html", context)


@login_required
def video_delete(request, video_id):
    video = Video.objects.filter(id=video_id)
    if video:
        video.delete()
    return HttpResponseRedirect(reverse("Videos:video_list"))
