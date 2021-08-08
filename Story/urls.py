from django.urls import path, re_path, include

from .views import *
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

app_name = 'Story'
urlpatterns = [
                  path(r'', storyList, name='storyList'),
                  path(r'_sort_by=<str:sort_by>', storyListSortBy, name='storyListSortBy'),
                  path(r'story_id=<int:story_id>', getStory, name='getStory'),
                  path(r'category=<str:category>_sort_by=<str:sort_by>_title=<str:title>', storyFind, name='storyFind'),
                  path(r'category=<str:category>_sort_by=<str:sort_by>', storyListCategorySortBy,
                       name='storyListCategorySortBy'),
                  path(r'category=<str:category>', storyListCategory, name='storyListCategory'),
                  path(r'upload/', upload, name='upload'),
                  path(r'advancedSearch=T', advancedSearch, name='advancedSearch'),
                  path(r'search/', search, name='search'),
                  path(r'edit=<int:story_id>', edit, name='edit'),
                  path(r'delete=<int:story_id>', delete, name="delete"),
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
