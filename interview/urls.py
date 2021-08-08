from django.contrib import admin
from django.urls import path, re_path
from meeting.models import Link
from interview import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('new_interview/<int:story_id>', views.new_interview, name='new_interview'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]
