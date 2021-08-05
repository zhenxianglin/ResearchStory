from django import forms
from forum.models import Forum
from ckeditor.fields import RichTextField


class ForumForm(forms.ModelForm):
    title=forms.CharField(label='title', max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Please enter your title'})
                 )
    text = RichTextField()
    class Meta:
        model = Forum
        fields = (
            'title',
            'text',
        )
        widgets = {'text': forms.Textarea(attrs={'cols': 70})}