from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    title = models.CharField(max_length=128)

    created_time = models.DateTimeField(auto_now_add=True)

    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created_time']
