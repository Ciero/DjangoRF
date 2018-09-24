from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.knowledge.serializers import KnowledgeSerializer
from project.api.user_profile.serializers import UserSerializer
from project.knowledge.models import Knowledge

User = get_user_model()


class SearchView(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        # data = request.data
        # type = data.get('type')
        # search_string = data.get('search_string')
        # category = data.get('category')

        # if type == 'knowledges':
        #     if category is None:
        #         knowledges = Knowledge.objects.filter(name__icontains=search_string)
        #     else:
        #         knowledges = Knowledge.objects.filter(name__icontains=search_string, category=category)
        #     serializer = KnowledgeSerializer(instance=knowledges, many=True)
        #     return Response(serializer.data)
        # elif type == 'users':
        #     users = User.objects.filter(username__icontains=search_string)
        #     serializer = UserSerializer(instance=users, many=True)
        #     return Response(serializer.data)
        # else:
        #     return Response('OK')
        
        
        search = request.query_params.get('search')
        knowledges = Knowledge.objects.filter(title__icontains=search)
        serializer = KnowledgeSerializer(instance=knowledges, many=True)
        return Response(serializer.data)

