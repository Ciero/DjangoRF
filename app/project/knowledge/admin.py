from django.contrib import admin
from project.knowledge.models import Knowledge



@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user']
    search_fields = ['category', 'title']
