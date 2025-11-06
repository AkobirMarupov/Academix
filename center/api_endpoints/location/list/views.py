from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from center.models import Location
from center.api_endpoints.location.list.serializers import LocationListeSerializers


class LocationListAPIView(APIView):
    parser_classes = []
    def get(self, request):
        location = Location.objects.all()
        serializer = LocationListeSerializers(location, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class LocationRetrievAPIView(APIView):
    parser_classes = []

    def get(self, request, pk):
        try:
            location = Location.objects.get(pk = pk)
        except Location.DoesNotExist:
            return Response({'detail': 'Malumot topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LocationListeSerializers(location)
        return Response(serializer.data, status=status.HTTP_200_OK)
        