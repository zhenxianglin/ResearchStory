from django.db import models
from Story.models import Story
from Users.models import User


# Create your models here.

class Interview(models.Model):
    interview_name = models.CharField(max_length=500)

    related_story_name = models.ForeignKey(Story, on_delete=models.CASCADE)

    interview_link = models.URLField(max_length=2000)

    start_time = models.TimeField(default='12:00:00')
    end_time = models.TimeField(default='12:00:00')

    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)

    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_added',)

    def __str__(self):
        return self.interview_name
