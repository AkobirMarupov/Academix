from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from course.models import Homework


class HomeworkDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            homework = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response({'detail': 'Bundaty homework topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        
        homework.delete()
        return Response({'detail': 'Malumot muvaffaqiyatli uchirildi.'}, status=status.HTTP_204_NO_CONTENT)