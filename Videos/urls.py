from django.urls import path
from Videos import views

app_name = 'Videos'
urlpatterns = [
    path('video_list/', views.VideoIndexView.as_view(), name='video_list'),

    path('video_list/<int:video_id>/', views.video_detail, name='video_detail'),

    path('video_list/post_comment/<int:video_id>/', views.post_video_comment, name='video_comment'),

    path('new_video/', views.new_video, name = 'new_video'),

    path("edit_video/<int:video_id>/",views.edit_video, name = 'edit_video'),

    path(r'video_delete=<int:video_id>', views.video_delete, name="video_delete"),

]
