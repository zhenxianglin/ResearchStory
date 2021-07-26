from django.conf.urls import url
from django.urls import path

from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Story'
urlpatterns = [
    path(r'', storyList, name='storyList'),
    path(r'_sort_by=<str:sort_by>', storyListSortBy, name='storyListSortBy'),
    path(r'story_id=<int:story_id>', getStory, name='getStory'),

    path(r'category=<str:category>_sort_by=<str:sort_by>', storyListCategorySortBy, name='storyListCategorySortBy'),
    path(r'category=<str:category>', storyListCategory, name='storyListCategory'),
    path(r'upload/', upload, name='upload'),
    path(r'advanced_search/', advancedSearch, name='advancedSearch'),
    path(r'search/', search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

