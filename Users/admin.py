from django.contrib import admin
from Users.models import User, Profile

"""register the models(tables) saved in database to the admin user (superuser)"""
admin.site.register(User)
admin.site.register(Profile)
