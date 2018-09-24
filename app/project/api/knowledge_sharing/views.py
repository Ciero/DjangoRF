from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.db.models import Q
from django.http import Http404
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import KnowledgeSharingSerializer
from project.api.user_profile.serializers import UserSerializer
from project.knowledge_sharing.models import KnowledgeSharing
from .permissions import IsReceiverOrReadOnly

User = get_user_model()


class KnowledgeRequestsListView(ListAPIView):
    serializer_class = KnowledgeSharingSerializer
    queryset = KnowledgeSharing.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(
            Q(status='pending'),
            Q(receiver=self.request.user)
        )
        return queryset


class SendKnowledgeRequestView(GenericAPIView):
    serializer_class = KnowledgeSharingSerializer
    queryset = User.objects.all()

    def post(self, request, **kwargs):
        user = self.get_object()
        # todo: make sure you can only send request to others, only send request if not existing
        serializer = self.get_serializer()
        f_request = serializer.save(
            sender=request.user,
            receiver=user,
        )
        return Response(KnowledgeSharingSerializer(f_request).data)


# class SendKnowledgeRequestView(APIView):
#     def get_object(self, user_id):
#         try:
#             receiver = User.objects.get(id=user_id)
#             return receiver
#         except User.DoesNotExist:
#             raise Http404
# 
#     def send_email(self, email, sender):
#         message = EmailMessage(
#             subject='You have a new knowledge  sharing request',
#             body=f'{sender} wold like to change services',
#             to=[email],
#         )
#         message.send()
# 
#     def post(self, request, user_id):
#         receiver = self.get_object(user_id)
#         if KnowledgeSharing.objects.filter(sender=request.user, receiver=receiver):
#             return Response('Already changed services or request pending')
#         if KnowledgeSharing.objects.filter(sender=receiver):
#             return Response('You can\'t change with yourself')
#         KnowledgeSharing.objects.create(sender=request.user, receiver=receiver)
#         self.send_email(receiver.email, request.user.username)
#         return Response('Knowledge sharing request sent')



class ListPendingKnowledgeRequestsView(ListAPIView):
    serializer_class = KnowledgeSharingSerializer
    queryset = KnowledgeSharing.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(
            Q(status='pending'),
            Q(sender=self.request.user)
        )
        return queryset


class KnowledgeRequestAcceptView(GenericAPIView):
    serializer_class = KnowledgeSharingSerializer
    queryset = KnowledgeSharing.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsReceiverOrReadOnly,
    ]

    def post(self, request, *args, **kwargs):
        knowledge_request = self.get_object()
        knowledge_request.status = 'accepted'
        knowledge_request.save()
        return Response(self.get_serializer(knowledge_request).data)


class KnowledgeRequestRejectView(GenericAPIView):
    serializer_class = KnowledgeSharingSerializer
    queryset = KnowledgeSharing.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsReceiverOrReadOnly,
    ]

    def post(self, request, *args, **kwargs):
        knowledge_request = self.get_object()
        knowledge_request.status = 'rejected'
        knowledge_request.save()
        return Response(self.get_serializer(knowledge_request).data)


class ListAllKnowledgeChanges(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(
            Q(sender=self.request.user),
            Q(status='pending')|
            Q(status='accepted')|
            Q(status='rejected')
        ).exclude(id=self.request.user.id).distinct()
        return queryset
