from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from course.models import Homework
from course.api_endpoints.homework.create.serializers import HomeworkCreateSerializer
from course.models import Course


class HomeworkCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        request_body=HomeworkCreateSerializer,
        responses={201: HomeworkCreateSerializer()},
        operation_description="Yangi uyga vazifa yaratish (faqat teacher, center_admin yoki superadmin uchun)"
    )
    def post(self, request):
        user = request.user

        if not (user.is_teacher or user.is_center_admin or user.is_superadmin):
            return Response(
                {"detail": "Sizga uyga vazifa yuklashga ruxsat berilmagan."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = HomeworkCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
