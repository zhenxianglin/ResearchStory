from django.contrib import admin
from django.urls import path
from meeting.models import Link
from interview import views


urlpatterns = [
    path('new_interview/<int:story_id>', views.new_interview, name='new_interview'),
]
