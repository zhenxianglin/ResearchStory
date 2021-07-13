from django.db import models
from django.utils.translation import ugettext_lazy as uget


class Account(models.Model):
    username = models.CharField("username", max_length=10, default="Null")
    age = models.IntegerField("age", default=-1)
    gender = models.CharField("gender", max_length=1, choices=(('M', 'Male'), ('F', 'Female')),
                              blank=True, null=True)
    last_name = models.CharField("Last Name", max_length=50, default="Null")
    first_name = models.CharField("First Name", max_length=50, default="Null")
    e_mail = models.CharField("e-mail", max_length=100, default="Null")
    password = models.CharField(uget("password"), max_length=128, default="Null")

    def __str__(self):
        return self.username
