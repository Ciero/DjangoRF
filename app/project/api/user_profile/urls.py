from django.urls import path
from .views import UserProfileView, ListUsersView, UpdateUserProfileView, UserByIdView, UserBySearchView

app_name = 'users'
urlpatterns = [
    
    path('me/', UserProfileView.as_view(), name='get_userprofile'),
    path('me/update/', UpdateUserProfileView.as_view(), name='update_userprofile'),

    path('list/', ListUsersView.as_view(), name='all_user_list'),
    path('search/', UserBySearchView.as_view(), name='user_by_search'),
    path('<int:user_id>/', UserByIdView.as_view(), name='user_by_id'),

]
  