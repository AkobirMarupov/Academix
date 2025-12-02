from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from groups.api_endpoints.group.update.serializers import GroupUpdateSerializer
from groups.models import Group



class GrioupUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Update a new Student",
        request_body=GroupUpdateSerializer,
        responses={
            200: openapi.Response("Group updated", GroupUpdateSerializer),
            400: "Notugri malumot yuborildi",
            401: "Avtorizatsiya talab etiladi",
            403: "Ruxsat yo'q",
        },
        tags=[],
    )

    def put(self, request, pk):
        user = request.user

        if not (user.is_superadmin or user.is_center_admin):
            return Response(
                {"detail": "Sizda ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            group = Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            return Response({'detail': 'Student topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = GroupUpdateSerializer(group, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Ma'lumot muvaffaqiyatli yangilandi.", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
