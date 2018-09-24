from rest_framework import serializers

from project.api.user_profile.serializers import UserSerializer
from project.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    comment_receiver = UserSerializer(
        required=False,
    )
    class Meta:
        model = Comment
        fields = ['content', 'comment_sender', 'date_created']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
