from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from center.models import Teacher
from center.api_endpoints.teacher.update.serializers import TeacherUpdateSerializers



class TeacherUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Update your own center information",
        operation_description="Allows an authenticated user to update their own center details.",
        request_body=TeacherUpdateSerializers,
        responses={
            200: openapi.Response('Center successfully updated.', TeacherUpdateSerializers),
            400: "Invalid input data",
            403: "You are not allowed to edit this center",
            404: "Center not found"
        },
        tags=[]
    )

    def put(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({'detail': 'Ustoz topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        
        if teacher.owner != request.user:
            return Response(
                {'detail': 'Sizda bu malumotni tahrirlash uchun ruxsat yuq.'},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = TeacherUpdateSerializers(teacher, data=request.data, partial= True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'detail': 'Malumotlare muvafaqqiyatli yangilandi.'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)