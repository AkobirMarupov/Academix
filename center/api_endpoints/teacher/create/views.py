from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from center.models import Teacher
from center.api_endpoints.teacher.create.serializers import TeacherCreateSerializers


class TeacherCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser] 

    @swagger_auto_schema(
        operation_summary="Create a new teacher",
        operation_description="Allows an authenticated user to create a new teacher for a center.",
        request_body=TeacherCreateSerializers,
        responses={
            201: openapi.Response('Teacher created successfully.', TeacherCreateSerializers),
            400: "Invalid input data"
        },
        tags=[]
    )

    def post(self, request):
        serializer = TeacherCreateSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(owner= request.user)
            return Response(
                {"detail": "Teacher muvafaqqiyatli yaratildi!", "data": serializer.data}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        