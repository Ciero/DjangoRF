from django.urls import path

from .views import ListKnowledgeView, ListKnowledgeCategoriesView, CreateKnowledgeView, GetUpdateDeleteKnowledgeByID, \
    ListKnowledgeByCategoryView, ListKnowledgeByUser

app_name = 'knowledge'

urlpatterns = [
    # GET request
    path('', ListKnowledgeView.as_view(), name='list_knowledge_view'),
    path('categories/', ListKnowledgeCategoriesView.as_view(),
         name='list_knowledge_categories_view'),
    # POST request
    path('new/', CreateKnowledgeView.as_view(), name='create_knowledge_view'),
    # GET request
    path('category/<str:category>/', ListKnowledgeByCategoryView.as_view(),
         name='knowledge_by_category_view'),
    # GET request
    path('user/<int:user_id>/', ListKnowledgeByUser.as_view(),
         name='knowledge_by_user_view'),
    # GET, POST and DELETE requests
    path('<int:pk>/', GetUpdateDeleteKnowledgeByID.as_view(),
         name='knowledge_detail_by_ID_view'),
]
