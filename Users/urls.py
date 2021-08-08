from django.conf.urls import url
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

from Users import views

app_name = 'Users'

urlpatterns = [
    # Login interface
    path(r'login/', LoginView.as_view(template_name='Users/login.html'), name='login'),

    path(r'logout/', views.logout_view, name='logout'),

    path(r'register/', views.register, name='register'),

    path(r'edit/<int:user_id>/', views.profile_edit, name='edit'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

]
