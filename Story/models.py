import os

from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from Users.models import User


class Story(models.Model):
    title_name = models.CharField(verbose_name="title", max_length=100)
    created_time = models.DateTimeField(verbose_name='publish time', auto_now_add=True)
    category = models.CharField(verbose_name="category", max_length=100,
                                choices=(('ComputerScience', 'ComputerScience'),
                                         ('Physics', 'Physics'),
                                         ("ElectricalEngineering", "ElectricalEngineering"),
                                         ),
                                blank=False, null=True)
    views = models.PositiveIntegerField(verbose_name='views number', default=0, auto_created=True)
    img= models.ImageField(verbose_name="front page", upload_to='img/', null=True)
    text = RichTextField()

    video = models.URLField(verbose_name="video", blank=True, null=True)
    paper_link = models.URLField(verbose_name="paper_link", null=True, blank=True)

    author = models.CharField(verbose_name="author", max_length=100,default='author')
    author_intro = models.CharField(verbose_name="author_intro", max_length=1000,default='author introduction')
    background = models.CharField(verbose_name="background", max_length=1000,default='background')
    tags = models.CharField(verbose_name="tags", max_length=100,default=category)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1', null=True)


    def __str__(self):
        return self.title_name

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        verbose_name_plural = 'Stories'

    def get_absolute_url(self):
        return reverse('Story:getStory', args=[self.id])



