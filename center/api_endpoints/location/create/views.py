from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser

from center.models import Location
from center.api_endpoints.location.create.serializers import LocationCreateSerializers


class LocationCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create a new Center",
        request_body=LocationCreateSerializers,
        responses={
            201: openapi.Response(
                description="Center created successfully",
                schema=LocationCreateSerializers()
            ),
            400: "Notugri malumot yuborildi",
            401: "Avtorizatsiya talab etiladi",
        },
        tags=[],
    )

    def post(self, request):
        serializer = LocationCreateSerializers(data=request.data , context={'request': request})
    
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(
                {
                    "message": "Location muvaffaqiyatli yaratildi!",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
