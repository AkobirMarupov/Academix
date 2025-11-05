from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from center.models import Center
from center.api_endpoints.center.list.serializers import CenterLisSerializers


class CenterLIstAPIView(APIView):
    parser_classes = []

    def get(self, request):
        centers = Center.objects.all()
        serializer = CenterLisSerializers(centers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CenterRetrieveAPIView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            center = Center.objects.get(pk = pk)
        except Center.DoesNotExist:
            return Response({"detail": "Center topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = CenterLisSerializers(center)
        return Response(serializer.data, status=status.HTTP_200_OK)