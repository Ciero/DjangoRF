from django.contrib import admin
from project.knowledge_sharing.models import KnowledgeSharing


@admin.register(KnowledgeSharing)
class KnowledgeSharingAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'status']
