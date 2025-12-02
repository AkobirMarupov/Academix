from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from groups.api_endpoints.group.create.serializers import GroupCreateSerializer
from groups.models import Group



class GroupCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create a new Group",
        request_body=GroupCreateSerializer,
        responses={
            201: openapi.Response(
                description="Group created successfully",
                schema=GroupCreateSerializer()
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
        
        serializer = GroupCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'massage': 'Guruh muvafaqqiyatli yaratildi', 'detail': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
