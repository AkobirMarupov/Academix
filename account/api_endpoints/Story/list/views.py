from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from account.api_endpoints.Story.list.serializers import StoryListSerializer
from account.models import Story



class StoryListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        story = Story.objects.all()
        serializer = StoryListSerializer(story, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class StoryRetriewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            story = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Response({"detail": "Story topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = StoryListSerializer(story)
        return Response(serializer.data, status=status.HTTP_200_OK)