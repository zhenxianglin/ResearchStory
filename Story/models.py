from django.db import models
from django.utils.timezone import now
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Story(models.Model):
    title_name = models.CharField(verbose_name="title", max_length=100)
    created_time = models.DateTimeField(verbose_name='publish time', auto_now_add=True)
    category = models.CharField(verbose_name="category", max_length=100,
                                choices=(('ComputerScience', 'ComputerScience'),
                                         ('Physics', 'Physics'),
                                         ("ElectricalEngineering", "ElectricalEngineering")),
                                blank=False, null=False)

    views = models.PositiveIntegerField(verbose_name='views number', default=0)

    text = models.TextField(verbose_name="text", blank=True, null=True)
    # video = models.CharField("video", max_length=9000)
    paper_link = models.CharField(verbose_name="paper_link", max_length=9000, null=True)

    def __str__(self):
        return self.title_name

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        verbose_name_plural = 'Stories'
