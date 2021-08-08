from django.db import models
from Users.models import User


class Link(models.Model):
    meeting_name = models.CharField(max_length=500)
    meeting_link = models.URLField(max_length=2000)

    start_time = models.TimeField(default='12:00:00')
    end_time = models.TimeField(default='12:00:00')

    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_added',)

    def __str__(self):
        return self.meeting_name
