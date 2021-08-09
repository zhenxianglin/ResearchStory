from django.db import models
import os

from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from Users.models import User
from mptt.models import MPTTModel, TreeForeignKey

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Forum(models.Model):
    title = models.CharField(verbose_name="title", max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='created_time', auto_now=True)
    text = models.TextField()
    views=models.PositiveIntegerField(verbose_name='views', default=0, auto_created=True)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('forum:get_forum', args=[self.id])


class ForumComment(MPTTModel):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments1')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments1')
    # mptt tree structure
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children1')
    # 记录二级评论回复给谁， str
    reply_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='replyers1')
    body = models.TextField()
    # body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ('-created',)
    class MPTTMeta:
        order_insertion_by = ['-created']

    def __str__(self):
        return self.body[:50]





