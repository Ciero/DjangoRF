from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.knowledge.serializers import KnowledgeSerializer, KnowledgeCategorySerializer
from project.knowledge.models import Knowledge


class ListKnowledgeView(generics.ListAPIView):
    """
    GET: Knowledge api view (returns all the Knowledge)
    """
    serializer_class = KnowledgeSerializer
    queryset = Knowledge.objects.all()
    permission_classes = []


class CreateKnowledgeView(generics.GenericAPIView):
    """
    POST: Create a new Knowledge
    """
    serializer_class = KnowledgeSerializer

    # Override POST method when using GenericAPIView
    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        post = serializer.create(serializer.validated_data)
        return Response(KnowledgeSerializer(post).data)


class ListKnowledgeCategoriesView(APIView):
    """
    GET: Lists all the Knowledgecategories
    """
    serializer_class = KnowledgeCategorySerializer

    def get(self, request, *args, **kwargs):
        """

        :rtype: 
        """
        categories = map(lambda x: {'name': x[1]}, Knowledge.CATEGORIES)
        return Response(self.serializer_class(categories, many=True).data)


class ListKnowledgeByCategoryView(ListAPIView):
    """
    GET: List all Knowledge
    """
    serializer_class = KnowledgeSerializer
    permission_classes = []

    def get_queryset(self):
        return Knowledge.objects.filter(category=self.kwargs['category'])


class GetUpdateDeleteKnowledgeByID(RetrieveUpdateDestroyAPIView):
    """
    GET PUT PATCH DELETE: Gets, updates or deletes a Knowledge by its ID
    """
    serializer_class = KnowledgeSerializer
    queryset = Knowledge.objects.all()


class ListKnowledgeByUser(ListAPIView):
    """
    GET: Lists all Knowledge created by a specific user
    """
    serializer_class = KnowledgeSerializer
    permission_classes = []

    def get_queryset(self):
        return Knowledge.objects.filter(user=self.kwargs['user_id'])
