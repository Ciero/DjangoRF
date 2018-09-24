from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UpdateUserProfileSerializer
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


class UserProfileView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        user = request.user
        return Response(self.get_serializer(user).data)


class UpdateUserProfileView(GenericAPIView):
    serializer_class = UpdateUserProfileSerializer

    def post(self, request):
        print(request.data)
        serializer = self.get_serializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.get_serializer(user).data)

class ListUsersView(APIView):
    permission_classes = []

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    
class UserBySearchView(APIView):
    permission_classes = []

    def get(self, request):
        search = request.query_params.get('search')
        if search:
            users = User.objects.filter(username__contains=search)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserByIdView(APIView):
    permission_classes = []

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer(user)
        return Response(serializer.data)
