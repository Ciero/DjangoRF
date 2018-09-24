from rest_framework import serializers

from project.api.user_profile.serializers import UserSerializer
from project.api.knowledge.serializers import KnowledgeSerializer
from project.rating.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Rating
        fields = ['user', 'knowledge', 'receiver', 'rating', 'date_created']

    def create(self, validated_data):
        return Rating.objects.create(**validated_data, user=self.context.get('request').user)
