from django.conf.urls import url
from django.urls import path

from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', storyList, name='storyList'),
    path(r'story_id=<int:story_id>', getStory, name='getStory'),
    path(r'category=<str:category>', storyListCategory, name='storyListCategory'),
    path(r'upload/',upload,name='upload'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  ## 没有这一句无法显示上传的图片(有也没用)

