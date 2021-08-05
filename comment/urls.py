from django.urls import path, include
from django.conf.urls import url
from comment import views
app_name = 'comment'

urlpatterns = [

    path(r'post_comment/<int:story_id>', views.post_comment, name='post_comment'),
    path(r'post_comment=<int:story_id>/<int:parent_comment_id>', views.post_comment, name='comment_reply'),

]
