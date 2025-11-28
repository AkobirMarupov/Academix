from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from students.api_adpoints.Student.create.serializers import StudentCreateSerializers
from students.models import Student



class StudentCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create a new Student",
        request_body=StudentCreateSerializers,
        responses={
            201: openapi.Response(
                description="Student created successfully",
                schema=StudentCreateSerializers()
            ),
            400: "Notugri malumot yuborildi",
            401: "Avtorizatsiya talab etiladi",
            403: "Ruxsat yo'q",
        },
        tags=[],
    )

    def post(self, request):

        user = request.user

        if not (user.is_superadmin or user.is_center_admin):
            return Response(
                {"detail": "❌ Sizda student yaratish uchun ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = StudentCreateSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Student muvaffaqiyatli yaratildi!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
