from django.db import models


class User(models.Model):
    username = models.CharField("username", max_length=10, unique=True, default="Null")
    age = models.IntegerField("age", null=True)
    gender = models.CharField("gender", max_length=1, choices=(('M', 'Male'), ('F', 'Female')),
                              blank=True, null=True)
    last_name = models.CharField("Last Name", max_length=50)
    first_name = models.CharField("First Name", max_length=50)
    e_mail = models.CharField("e-mail", max_length=100, unique=True)
    password = models.CharField("password", max_length=128, unique=True)
    ticket = models.CharField("ticket", max_length=30, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"



#dklhkjhasd
