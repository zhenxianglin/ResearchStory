from django.db import models
from embed_video.fields import EmbedVideoField
from Users.models import User
from Story.models import Story
from django.urls import reverse
from .validators import file_size


class Classification(models.Model):
    list_display = ('title')
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'v_classification'

    def __str__(self):
        return str(self.title)


class Video(models.Model):
    title = models.CharField(max_length=228)
    desc = models.TextField(blank=True, null=True)

    url = EmbedVideoField(blank=True, null=True)

    file = models.FileField(upload_to='video/%y', validators=[file_size], blank=True, null=True)

    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True)

    uploader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created_time']

    def get_absolute_url(self):
        return reverse('Videos:video_detail', args=[self.id])


class VideoComment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video_comments")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="video_comments")

    content = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.content[:30]
