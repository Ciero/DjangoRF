from rest_framework import serializers

from project.knowledge.models import Knowledge


class KnowledgeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Knowledge
        fields = ['id', 'title', 'category',  'image',
                  'user', 'description']
        read_only_fields = ['id', 'user']

    def get_image(self, knowledge):
        if knowledge.image:
            return knowledge.image.url
        return "Nope"

    def create(self, validated_data):
        return Knowledge.objects.create(**validated_data, user=self.context.get('request').user)


class KnowledgeCategorySerializer(serializers.Serializer):
    name = serializers.CharField()
