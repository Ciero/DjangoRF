from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import RatingSerializer


class CreateRatingOnKnowledgeAPIView(GenericAPIView):
    serializer_class = RatingSerializer
    permission_classes = [] 
    
    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        rating = serializer.create(serializer.validated_data)
        return Response(RatingSerializer(rating).data)
