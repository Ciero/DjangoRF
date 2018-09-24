from django.urls import path

from .views import  KnowledgeRequestsListView, SendKnowledgeRequestView, ListPendingKnowledgeRequestsView, KnowledgeRequestAcceptView, KnowledgeRequestRejectView, ListAllKnowledgeChanges

app_name = 'knowledge_sharing'

urlpatterns = [
   
    path('knowledgerequests/', KnowledgeRequestsListView.as_view(), name='list_all_knowledge_requests'),
    path('knowledgerequest/<int:pk>/', SendKnowledgeRequestView.as_view(), name='send_knowledge_request'),
    
    path('knowledgerequests/pending/', ListPendingKnowledgeRequestsView.as_view(), name='pending_requests'),
    path('knowledgerequests/accept/<int:request_id>/', KnowledgeRequestAcceptView.as_view(),name='accept_request'),
    path('knowledgerequests/reject/<int:request_id>/', KnowledgeRequestRejectView.as_view(),name='reject_request'),
   
    
    path('knowledgesharing/', ListAllKnowledgeChanges.as_view(), name='list_all_my_knowledgechanges'),

]