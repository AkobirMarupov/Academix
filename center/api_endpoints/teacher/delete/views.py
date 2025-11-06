from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


from center.models import Teacher


class TeacherDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({'detail': 'Ustoz topilmadi.'},tatus=status.HTTP_404_NOT_FOUND)
        
        if teacher.owner != request.user:
            return Response(
                {'detail': 'Sizda bu malumotlarni uchirolmaysz.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        teacher.delete()
        return Response(
            {'detail': 'Ustoz muvaffaqiyatli uchirildi.'},
            status=status.HTTP_204_NO_CONTENT
        )