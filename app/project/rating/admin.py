from django.contrib import admin
from project.rating.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating', 'user', 'user_id', 'receiver','receiver_id', 'knowledge', 'knowledge_id']