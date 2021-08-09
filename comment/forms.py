from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    """generate a comment form under the research story page"""
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {'body': forms.Textarea(attrs={'cols': 70})}