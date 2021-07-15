from django.db import models
from django.contrib.auth.models import AbstractUser, User as  User_view


class User(AbstractUser):
    SEX_ITEMS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ("S", 'Secret'),
    )

    ROLES = (
        ('R', 'Researcher'),
        ('C', 'Common User'),
    )

    username = models.CharField(max_length=128, unique=True, verbose_name='username')
    age = models.IntegerField(null=True, verbose_name="age")
    gender = models.CharField(choices=SEX_ITEMS, max_length=100, verbose_name="gender")

    last_name = models.CharField(max_length=128, verbose_name="last Name")
    first_name = models.CharField(max_length=128, verbose_name="first Name")

    usertype = models.CharField(choices=ROLES, max_length=100, verbose_name='user type')
    email = models.EmailField(unique=True, verbose_name="email", )

    password = models.CharField(max_length=256, verbose_name='password')

    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created time')

    def __str__(self):
        # Help humanized display object information
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = "users"
