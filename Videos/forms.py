from django import forms
from Videos.models import VideoComment, Video, Classification


class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ['content']


class NewVideoForm(forms.ModelForm):
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
