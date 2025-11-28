from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from students.api_adpoints.Student.update.serializers import StudentUpdateSerializers
from students.models import Student


class StudentUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Update Student",
        request_body=StudentUpdateSerializers,
        responses={
            200: openapi.Response("Student updated", StudentUpdateSerializers),
            400: "Bad request",
            401: "Unauthorized",
            403: "Permission denied"
        }
    )
    def put(self, request, pk):

        user = request.user
        if not (user.is_superadmin or user.is_center_admin):
            return Response(
                {"detail": "Sizda ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'detail': 'Student topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentUpdateSerializers(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Ma'lumot muvaffaqiyatli yangilandi.", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
