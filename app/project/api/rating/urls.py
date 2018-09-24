from django.urls import path
from .views import CreateRatingOnKnowledgeAPIView

app_name = 'rating'
urlpatterns = [
    path('', CreateRatingOnKnowledgeAPIView.as_view(), name='create-rating-on-knowledge')
]