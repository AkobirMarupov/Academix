from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from account.api_endpoints.Profile.list.serializers import ProfileListSerializer
from account.models import Profile



class ProfileListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileListSerializer(print, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



class ProfileRetriewAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = ProfileListSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
