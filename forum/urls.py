"""ResearchStory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, re_path
from forum import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf import settings

app_name = 'forum'

urlpatterns = [
    path(r'', forumList, name='forumList'),
    path(r'forum_id=<int:forum_id>', get_forum, name='get_forum'),
    path(r'post_forum/<int:forum_id>', post_forum, name='post_forum'),
    path(r'post_forum/<int:forum_id>/<int:parent_forumcomment_id>', post_forum, name='forum_reply'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
