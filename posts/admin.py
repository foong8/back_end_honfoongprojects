from django.contrib import admin
from .models import Post, Comment, Progress, ActionItem,HistoryLog

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Progress)
admin.site.register(ActionItem)
admin.site.register(HistoryLog)