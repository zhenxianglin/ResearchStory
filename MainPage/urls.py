"""定义Main Page的URL 的模式"""

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from MainPage import views
from django.urls import path, include

urlpatterns = [
    # 主页
    # path('index/', views.index, name='index'),

    url(r'^$', views.index, name='index'),

]
