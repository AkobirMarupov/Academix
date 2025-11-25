from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from course.models import Homework
from course.api_endpoints.homework.list.serializers import HomeworkListSerializer


class HomeworkListAPIView(APIView):
    parser_classes = []

    def get(self, request):
        homework = Homework.objects.all()
        serializer = HomeworkListSerializer(homework, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class HomeworkRetrievAPIView(APIView):
    parser_classes = []

    def get(self, request, pk):
        try:
            homework = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response({'detail': 'Bunday homework topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = HomeworkListSerializer(homework)
        return Response(serializer.data, status=status.HTTP_200_OK)