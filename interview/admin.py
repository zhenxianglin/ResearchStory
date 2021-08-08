from django.contrib import admin
from interview.models import Interview

"""register the models(tables) saved in database to the admin user (superuser)"""

admin.site.register(Interview)
