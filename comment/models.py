from django.db import models
from Users.models import User
from Story.models import Story
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField


class Comment(MPTTModel):
    """create a comment table"""
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    # mptt tree structure
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    reply_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='replyers')
    body = models.TextField()
    # body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ('-created',)
    class MPTTMeta:
        order_insertion_by = ['-created']

    def __str__(self):
        return self.body[:50]
