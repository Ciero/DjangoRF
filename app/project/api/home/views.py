from rest_framework.generics import ListAPIView

from project.api.knowledge.serializers import KnowledgeSerializer
from project.knowledge.models import Knowledge


class HomeView(ListAPIView):
    serializer_class = KnowledgeSerializer
    permission_classes = []

    def get_queryset(self):
        return Knowledge.objects.all()