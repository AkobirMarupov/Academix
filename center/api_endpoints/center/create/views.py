from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser

from center.api_endpoints.center.create.serializers import CenterCreateSerializer
from center.models import Center


class CenterCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]  

    @swagger_auto_schema(
        operation_description="Create a new Center",
        request_body=CenterCreateSerializer,
        responses={
            201: openapi.Response(
                description="Center created successfully",
                schema=CenterCreateSerializer()
            ),
            400: "Notugri malumot yuborildi",
            401: "Avtorizatsiya talab etiladi",
        },
        tags=["Center Management"],
    )

    def post(self, request,):
        serializer = CenterCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(
                {"message": "Markaz muvaffaqiyatli yaratildi!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)