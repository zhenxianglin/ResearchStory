from django.db import models


class User(models.Model):
    SEX_ITEMS = [

        (1, 'Male'),
        (2, 'Female'),
        (0, 'Secret'),
    ]

    ROLES = [
        (0, 'Researcher'),
        (1, 'Common User'),
    ]

    username = models.CharField(max_length=128, unique=True, verbose_name='username')
    age = models.IntegerField(verbose_name="age", null=True)
    gender = models.IntegerField(verbose_name="gender", choices=SEX_ITEMS)

    last_name = models.CharField(max_length=128, verbose_name="last Name", )
    first_name = models.CharField(max_length=128, verbose_name="first Name")
    usertype = models.IntegerField(choices=ROLES, verbose_name='user type')
    email = models.EmailField(unique=True, verbose_name="email", )

    password = models.CharField(max_length=256, verbose_name='password')

    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created time')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'users'
        verbose_name_plural = "users"
