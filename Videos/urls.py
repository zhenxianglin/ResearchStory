from django.urls import path
from Videos import views

app_name = 'Videos'
urlpatterns = [

    path('video_list/', views.video_list, name='video_list'),

]
