from django.contrib import admin
from .models import Comment
from .actions import disapproved_comments, approved_comments


class AdminComment(admin.ModelAdmin):
    list_display = ['user', 'date_post', 'approved']
    actions = [disapproved_comments, approved_comments]


admin.site.register(Comment, AdminComment)
