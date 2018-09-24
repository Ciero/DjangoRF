from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_sender', 'comment_receiver', 'content',  'date_created']
    # search_fields = ['content']
