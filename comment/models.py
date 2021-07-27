from django.db import models
from Users.models import User
from Story.models import Story
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField


class Comment(MPTTModel):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    # mptt tree structure
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # 记录二级评论回复给谁， str
    reply_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='replyers')
    body = models.TextField()
    # body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     ordering = ('-created',)
    class MPTTMeta:
        order_insertion_by = ['-created']
    def __str__(self):
        return self.body[:50]


# class Comment(models.Model):
#     comment = models.TextField(max_length=500)
#
#     created_on = models.DateTimeField(auto_now_add=True, editable=False)
#
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)
#
#     likes = models.ManyToManyField(User,blank=True, related_name='comment_likes')
#
#     dislikes = models.ManyToManyField(User, blank=True, related_name="comment_dislikes")
#
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="+")
#
#     @property
#     def children(self):
#         return Comment.objects.filter(parent=self).order_by('-created_on').all()
#
#     @property
#     def is_parent(self):
#         if self.parent is None:
#             return True
#         return False
