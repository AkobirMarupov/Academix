from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from groups.api_endpoints.group.list.serializer import GroupListSerializer
from groups.models import Group



class GroupListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if not (user.is_superadmin or user.is_center_admin):
            return Response(
                {"detail": "Sizda ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )
    
        group = Group.objects.all()
        serializer = GroupListSerializer(group, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class GroupRetriewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = request.user

        if not (user.is_superadmin or user.is_center_admin):
            return Response(
                {"detail": "Sizda ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )
    
        try:
            group = Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            return Response(
                {'massage': 'Bunday guruh topilmadi yoki mavjud emas.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = GroupListSerializer(group)
        return Response(serializer.data, status=status.HTTP_200_OK)