from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from groups.api_endpoints.groupstudent.create.serializers import GroupStudetCreateSerializer
from groups.models import GroupStudent



class GroupStudetCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="GroupStudent a new Group",
        request_body=GroupStudetCreateSerializer,
        responses={
            201: openapi.Response(
                description="GroupStudent created successfully",
                schema=GroupStudetCreateSerializer()
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
                {"detail": "Sizda guruh yaratish uchun ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = GroupStudetCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'massage': 'Student guruhi muvafaqqiyatli yaratildi', 'detail': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)