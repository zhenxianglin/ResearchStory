from django.contrib import admin
from Videos.models import Video,Classification, VideoComment

from embed_video.admin import AdminVideoMixin


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, AdminVideo)
admin.site.register(Classification)
admin.site.register(VideoComment)
