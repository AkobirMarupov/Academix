from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from groups.api_endpoints.groupstudent.update.serializers import GroupStudetUpdateSerializer
from groups.models import GroupStudent

class GrioupStudentUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, pk):
        user = request.user

        if not (user.is_superadmin or user.is_center_admin):
            return Response(
                {"detail": "Sizda ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            gs = GroupStudent.objects.get(pk=pk)
        except GroupStudent.DoesNotExist:
            return Response(
                {'detail': 'GroupStudent topilmadi.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = GroupStudetUpdateSerializer(gs, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Ma'lumot muvaffaqiyatli yangilandi.", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
