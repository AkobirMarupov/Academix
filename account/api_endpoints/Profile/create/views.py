from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from account.api_endpoints.Profile.create.serializers import ProfileCreateSerializer
from account.models import Profile



class ProfileCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create a new Profile",
        request_body=ProfileCreateSerializer,
        responses={
            201: openapi.Response(
                description="Profile created successfully",
                schema=ProfileCreateSerializer()
            ),
            400: "Notugri malumot yuborildi",
            401: "Avtorizatsiya talab etiladi",
            403: "Ruxsat yo'q",
        },
        tags=[],
    )

    def post(self, request):
        serializer = ProfileCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'massage': 'Profile muvafaqqiyatli yaratildi', 'detail': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 