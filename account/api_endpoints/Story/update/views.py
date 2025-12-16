from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from account.api_endpoints.Story.update.serializers import StoryUpdateSerializer
from account.models import Story



class StoryUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Update your own Story information",
        operation_description="Allows an authenticated user to update their own Story details.",
        request_body=StoryUpdateSerializer,
        responses={
            200: openapi.Response('Story successfully updated.', StoryUpdateSerializer),
            400: "Invalid input data",
            403: "You are not allowed to edit this Story",
            404: "Story not found"
        },
        tags=[]
    )

    def put(self, request, pk):
        try:
            story = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Response({'massage': 'Bunday story topilmadi.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = StoryUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'massage': 'Malumot muvafaqqiyatli yangilandi.', 'data':serializer.data},
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)