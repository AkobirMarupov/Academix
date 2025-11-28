from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from students.models import Student
from students.api_adpoints.Student.list.serializers import StudentListSerializers


class StudentListAPIView(APIView):
    parser_classes = []

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentListSerializers(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class StudentRetrievAPIView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"detail": "Talaba topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentListSerializers(student)
        return Response(serializer.data, status=status.HTTP_200_OK)