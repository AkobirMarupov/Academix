from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from account.api_endpoints.Profile.update.serializers import ProfileUpdateeSerializer
from account.models import Profile


class ProfileUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Update your own Profile information",
        operation_description="Allows an authenticated user to update their own Profile details.",
        request_body=ProfileUpdateeSerializer,
        responses={
            200: openapi.Response('Profile successfully updated.', ProfileUpdateeSerializer),
            400: "Invalid input data",
            403: "You are not allowed to edit this Profile",
            404: "Profile not found"
        },
        tags=[]
    )

    def put(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(
                {'massage': 'Bunday profile topilmadi.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = ProfileUpdateeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'massage': 'Malumot muvafaqqiyatli yangilandi.', 'data':serializer.data},
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)