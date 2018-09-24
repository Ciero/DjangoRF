from django.urls import path
from .views import ListCommentsOnUserProfileAPIView, DeleteCommentAPIView, CreateCommentAPIView

app_name = 'comment'
urlpatterns = [
    path('<int:user_id>/', ListCommentsOnUserProfileAPIView.as_view(), name='list-comments-on-user-profile'),
    path('delete/<int:user_id>/', DeleteCommentAPIView.as_view(), name='delete-comments-what-I-was-created'),
    path('new/<int:user_id>/', CreateCommentAPIView.as_view(), name='create-comments-on-user-profile'), 
]
