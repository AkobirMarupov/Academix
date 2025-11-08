from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from course.models import Course
from course.api_endpoints.course.update.serializers import CourseListSerializers


class CourseUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Update your own center information",
        operation_description="Allows an authenticated user to update their own center details.",
        request_body=CourseListSerializers,
        responses={
            200: openapi.Response('Center successfully updated.', CourseListSerializers),
            400: "Invalid input data",
            403: "You are not allowed to edit this center",
            404: "Center not found"
        },
        tags=[]
    )

    def patch(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(
                {'detail': 'Malumot topilmadi.'},
                status=status.HTTP_404_NOT_FOUND
            )
        if course.owner != request.user:
            return Response({'detail': 'Siz bu malumotni tahrirlay olmaysiz.'},
            status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = CourseListSerializers(course, data=request.data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'detail': 'MAlumot muvaffaqiyatli yangilandi.', 'data': serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    