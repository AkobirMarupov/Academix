from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from center.models import Location
from center.api_endpoints.location.update.serializers import LocationUpdateSerializers


class LOcationUPdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Update your own center information",
        operation_description="Allows an authenticated user to update their own center details.",
        request_body=LocationUpdateSerializers,
        responses={
            200: openapi.Response('Center successfully updated.', LocationUpdateSerializers),
            400: "Invalid input data",
            403: "You are not allowed to edit this center",
            404: "Center not found"
        },
        tags=[]
    )

    def put(self, request, pk):
        try:
            location = Location.objects.get(pk = pk)
        except Location.DoesNotExist:
            return Response(
                {'detail': 'Joy topilmadi.'}, status=status.HTTP_404_NOT_FOUND
            )
        
        if location.created_by != request.user:
            return Response ({'detail': 'Siz ushbu joyni tahrirlash huquqiga ega emassiz.'},
            status=status.HTTP_403_FORBIDDEN
        )

        serializer = LocationUpdateSerializers(location, data= request.data, context={'request': request} , partial=True)

        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(
            {
                "message": "Location muvaffaqiyatli yangilandi!",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)