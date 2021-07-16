from django.db import models
from django.utils import timezone


class Story(models.Model):
    title_name = models.CharField("title_name", max_length=100)
    publish_time = models.DateTimeField('publish_time', auto_now=True)
    category = models.CharField("category", max_length=100,
                                choices=(('Computer Science', 'CS'),
                                         ('Physics', 'Physics'),
                                         ("Electrical Engineering", "EE")),
                                blank=True, null=True)

    # user_id = models.ForeignKey

    class Meta:
        verbose_name_plural = 'Stories'


class StoryContent(models.Model):
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="story_id")
    text = models.CharField("text", max_length=9000)
    video = models.CharField("video", max_length=9000)
    paper_link = models.CharField("paper_link", max_length=9000)

    class Meta:
        verbose_name_plural = 'StoryContents'