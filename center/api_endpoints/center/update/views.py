from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from center.api_endpoints.center.update.serializers import CenterUpdateSerializers
from center.models import Center

class CenterUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Update your own center information",
        operation_description="Allows an authenticated user to update their own center details.",
        request_body=CenterUpdateSerializers,
        responses={
            200: openapi.Response('Center successfully updated.', CenterUpdateSerializers),
            400: "Invalid input data",
            403: "You are not allowed to edit this center",
            404: "Center not found"
        },
        tags=[]
    )

    def put(self, request, pk):
        try:
            center = Center.objects.get(pk=pk)
        except Center.DoesNotExist:
            return Response({'detail': 'Center not found'}, status=status.HTTP_404_NOT_FOUND)
        

        if center.owner != request.user:
            return Response(
                 {"error": "You do not have permission to edit this center."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = CenterUpdateSerializers(center, data= request.data, partial= True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Center successfully updated.", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
