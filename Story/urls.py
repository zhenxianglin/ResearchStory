from django.conf.urls import url
from django.urls import path

from .views import *


urlpatterns = [
    path(r'', storyList, name='storyList'),
    path(r'<str:category>', storyListCategory, name='storyListCategory'),
    path(r'<int:story_id>', getStory, name='getStory'),
]

