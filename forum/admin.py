from django.contrib import admin
from django.contrib import admin

from forum.models import Forum
# Register your models here.
"""register the models(tables) saved in database to the admin user (superuser)"""

admin.site.register(Forum)