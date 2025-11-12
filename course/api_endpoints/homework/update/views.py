from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from course.models import Homework
from course.api_endpoints.homework.update.serializers import HomeworkUpdateSerializer


class HomeworkUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Update your own homevork information",
        operation_description="Allows an authenticated user to update their own homevork details.",
        request_body=HomeworkUpdateSerializer,
        responses={
            200: openapi.Response('homevork successfully updated.', HomeworkUpdateSerializer),
            400: "Invalid input data",
            403: "You are not allowed to edit this homevork",
            404: "homevork not found"
        },
        tags=[]
    )

    def put(self, request, pk):
        user = request.user
        try:
            homework = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response(
                {'detail': 'Malumot topilmadi.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if not (user.is_teacher or user.is_center_admin or user.is_superadmin):
            return Response(
                {"detail": "Sizga uyga vazifa yuklash ruxsat etilmagan."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = HomeworkUpdateSerializer(homework, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'detail': 'MAlumot muvaffaqiyatli yangilandi.', 'data': serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    