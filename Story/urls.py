from django.conf.urls import url
from django.urls import path

from .views import *


urlpatterns = [
    path(r'', storyList, name='storyList'),
    path(r'story_id=<int:story_id>', getStory, name='getStory'),
    path(r'category=<str:category>', storyListCategory, name='storyListCategory'),
    path(r'upload/',upload,name='upload'),
]

