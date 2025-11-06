from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from center.models import Teacher
from center.api_endpoints.teacher.list.serializers import TeacherListSerializers


class TeacherListAPIView(APIView):
    parser_classes = []

    def get(self, request):
        teacher = Teacher.objects.all()
        serializers = TeacherListSerializers(teacher, many= True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    


class TeacherRetriveAPIView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk = pk)
        except Teacher.DoesNotExist:
            return Response({'detail': 'Teacher Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeacherListSerializers(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)
