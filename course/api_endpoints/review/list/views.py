from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from course.models import Review
from course.api_endpoints.review.list.serializers import ReviewListSerializers


class ReviewListAPIView(APIView):
    parser_classes = []

    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewListSerializers(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ReviewRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({"detail": "Review topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReviewListSerializers(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
