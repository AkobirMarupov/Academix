from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from students.models import Student


class StudentDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        user = request.user

        if not (user.is_superadmin or user.is_center_admin):
            return Response(
                {"detail": "Sizda studentni o'chirish ruxsati yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"detail": "Student topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response({"message": "Student muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)
