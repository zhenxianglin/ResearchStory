from django.contrib import admin


from comment.models import Comment
"""register the models(tables) saved in database to the admin user (superuser)"""

admin.site.register(Comment)