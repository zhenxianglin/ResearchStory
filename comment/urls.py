from django.urls import path, include,re_path
from django.conf.urls import url
from comment import views
from django.views.static import serve
from django.conf import settings

app_name = 'comment'


urlpatterns = [

    path(r'post_comment/<int:story_id>', views.post_comment, name='post_comment'),
    path(r'post_comment/<int:story_id>/<int:parent_comment_id>', views.post_comment, name='comment_reply'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

]
