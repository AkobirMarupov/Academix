from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from course.models import Review


class ReviewDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(
                {'detail': "BUnday malumot topilmadi."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        user = request.user
        is_admin = user.is_superuser or user.is_staff
        is_teacher = hasattr(user, 'teacher')

        if not(is_admin or is_teacher == user):
            return Response(
                {'detail': 'Siz bu sharhni uchirishga ruxsatingiz yo‘q.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        review.delete()
        return Response(
            {'detail': 'Malumot muvaffaqiyatli uchirildi.'},
            status=status.HTTP_204_NO_CONTENT
        )
