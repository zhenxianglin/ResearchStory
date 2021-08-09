from django import forms
from Videos.models import VideoComment, Video, Classification


class VideoCommentForm(forms.ModelForm):
    """create a form for the comment of video"""
    class Meta:
        model = VideoComment
        fields = ['content']


class NewVideoForm(forms.ModelForm):
    """generate a form for uploading a new interview (meeting) video"""
    class Meta:
        model = Video
        fields = [
            'title',
            'desc',
            'url',
            'file',
            'classification',
        ]
        widgets = {'desc': forms.Textarea(attrs={'cols': 60})}
