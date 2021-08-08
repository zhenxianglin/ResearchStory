from django.contrib import admin
from django.urls import path
from meeting.models import Link
from meeting import views

app_name = 'meeting'

urlpatterns = [
    path(r'', views.current_meeting, name='current_meeting'),

    path(r'new_meeting', views.new_meeting, name='new_meeting'),

]
