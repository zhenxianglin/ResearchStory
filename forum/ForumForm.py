from django import forms
from forum.models import Forum


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = (
            'title',
            'text',
        )
        widgets = {'text': forms.Textarea(attrs={'cols': 70})}