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

class Forum(MPTTModel):
    title=models.CharField(verbose_name="title", max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_time=models.DateTimeField(verbose_name='created_time', auto_now=True)
    text=RichTextField()
    parent_comment = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='comm_par')
    reply_to_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='rep_to_user')
    views=models.PositiveIntegerField(verbose_name='views', default=0, auto_created=True)

    class MPTTMeta:
        order_insertion_by = ['created_time']

    def __str__(self):
        return self.title

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])





