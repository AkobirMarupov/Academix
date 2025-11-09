from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from course.api_endpoints.review.update.serializers import ReviewUpdateSerializers
from course.models import Review


class ReviewUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


    @swagger_auto_schema(
        operation_summary="Update your own center information",
        operation_description="Allows an authenticated user to update their own center details.",
        request_body=ReviewUpdateSerializers,
        responses={
            200: openapi.Response('Center successfully updated.', ReviewUpdateSerializers),
            400: "Invalid input data",
            403: "You are not allowed to edit this center",
            404: "Center not found"
        },
        tags=[]
    )

    def put(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(
                {'detail': 'Malumot topilmadi'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        user = request.user
        is_admin = user.is_superuser or user.is_staff
        is_teacher = hasattr(user, 'teacher')

        if not(is_admin or is_teacher == user):
            return Response(
                {'detail': 'Siz bu sharhni tahrirlashga ruxsatingiz yo‘q.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = ReviewUpdateSerializers(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                    {'detail': 'Sharh muvaffaqiyatli yangilandi.', 'data': serializer.data},
                    status=status.HTTP_200_OK
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
