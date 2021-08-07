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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'Users/', include(('Users.urls', 'Users'), namespace='Users')),

    path(r'', include(('MainPage.urls', 'MainPage'), namespace='MainPage')),

    path(r'story/', include(('Story.urls', 'Story'), namespace='Story')),

    path(r'comment/', include(('comment.urls', 'comment'), namespace='comment')),

    path(r'password_reset/', include('password_reset.urls')),
    path('accounts/', include('allauth.urls')),
    path('meeting/', include(('meeting.urls', 'meeting'), namespace='meeting')),

    path('', include(('interview.urls', 'interview'), namespace='interview')),
    path(r'forum/', include(('forum.urls', 'forum'), namespace='forum')),

    path(r'', include(('Videos.urls', 'Videos'), namespace='Videos')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
