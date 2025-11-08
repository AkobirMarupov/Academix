from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from course.models import Course
from course.api_endpoints.course.create.serializers import CourseCreateSerializers


class CourseCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create a new Center",
        request_body=CourseCreateSerializers,
        responses={
            201: openapi.Response(
                description="Center created successfully",
                schema=CourseCreateSerializers()
            ),
            400: "Notugri malumot yuborildi",
            401: "Avtorizatsiya talab etiladi",
        },
        tags=[],
    )

    def post(self, request):
        serializer = CourseCreateSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                {'detail': 'Course muvaffaqiyatli yaratildi.', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    