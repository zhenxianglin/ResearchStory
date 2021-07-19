from django.db import models
from Users.models import User
from Story.models import Story


# 评论
class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.body[:20]
