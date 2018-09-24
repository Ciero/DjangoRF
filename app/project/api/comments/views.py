from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, GenericAPIView

from project.comment.models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response



class ListCommentsOnUserProfileAPIView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = []

    def get_queryset(self):
        user_profile_id = self.kwargs['user_profile_id']
        return Comment.objects.filter(user_profile_id=user_profile_id)


class CreateCommentAPIView(GenericAPIView):
    serializer_class = CommentSerializer

    def post(self, request, user_profile_id):
        data = request.data.dict()
        data['user_profile'] = user_profile_id
        data['user'] = request.user.id
        serializer = self.get_serializer(
            data=data,
        )
        serializer.is_valid(raise_exception=True)
        post = serializer.create(serializer.validated_data)
        return Response(CommentSerializer(post).data)


class DeleteCommentAPIView(DestroyAPIView):
    # serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'  # is the actual field of the model
    lookup_url_kwarg = 'comment_id'  # is the input name inside the url








# class ListCommentsOnUserProfileAPIView(ListAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = []
# 
#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         return Comment.objects.filter(comment_receiver=user_id)
# 
# 
# # user_id is the receiver and the logged in user is the sender
# class DeleteCommentAPIView(DestroyAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = []
# 
#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         return Comment.objects.filter(comment_receiver=user_id, comment_sender=self.request.user)
# 
# 
# # user_id is going to be the receiver and sender will be the logged in user (request.user)
# class CreateCommentAPIView(CreateAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = []
# 
#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         return Comment.objects.filter(comment_receiver=user_id, comment_sender=self.request.user)
