from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from course.models import Course


class CourseDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Delete a center",
        operation_description="Allows an authenticated user to delete their own center by ID.",
        responses={
            204: "Center successfully deleted",
            403: "Not allowed to delete this center",
            404: "Center not found"
        },
        tags=[]
    )

    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(
                {'detail': 'BUnday malumot topilmadi.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if course.owner != request.user:
            return Response(
                {'detail': 'Siz bu malumotni uchirolmaysiz.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        course.delete()
        return Response(
            {'message': 'Malumot muvaffaqiyatli uchirildi.'},
            status=status.HTTP_204_NO_CONTENT
        )