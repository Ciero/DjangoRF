from rest_framework import serializers

from project.api.user_profile.serializers import UserSerializer
from project.knowledge_sharing.models import KnowledgeSharing
from django.core.mail import EmailMessage



class KnowledgeSharingSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = KnowledgeSharing
        fields = ['id', 'sender', 'receiver', 'status']
        read_only_fields = fields

    @staticmethod
    def send_notification(**kwargs):
        sender = kwargs.get('sender')
        receiver = kwargs.get('receiver')
        message = EmailMessage(
            subject='Knowledge sharing request was sent to you',
            body=f'The user {sender.username} has sent you a knowledge sharing!',
            to=[receiver.email],
        )
        message.send()

    def save(self, **kwargs):
        f_request = KnowledgeSharing.objects.create(**kwargs)
        self.send_notification(**kwargs)
        return f_request