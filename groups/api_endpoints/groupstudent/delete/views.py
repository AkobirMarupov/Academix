from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from groups.models import GroupStudent



class GroupStudentDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            group = GroupStudent.objects.get(pk=pk)
        except GroupStudent.DoesNotExist:
            return Response(
                {'massage': 'Bunday guruh topilmado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        user = request.user

        if not (user.is_superadmin or user.is_center_admin):
            return Response(
                {"detail": "Sizda ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        group.delete()
        return Response(
            {'message': 'Malumot muvaffaqiyatli uchirildi.'},
            status=status.HTTP_204_NO_CONTENT
        )