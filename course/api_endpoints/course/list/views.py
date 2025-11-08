from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from course.models import Course
from course.api_endpoints.course.list.serializers import CourseListSerializers


class CourseListAPIView(APIView):
    parser_classes = []
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseListSerializers(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CourseRetrievAPIView(APIView):
    parser_classes = []

    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(
                {'detail': 'BUnday malumot topilmadi.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CourseListSerializers(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    