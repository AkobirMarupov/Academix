from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from center.models import Location


class LocatinDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Delete a center",
        operation_description="Allows an authenticated user to delete their own center by ID.",
        responses={
            204: "Center successfully deleted",
            403: "Not allowed to delete this center",
            404: "Center not found"
        },
        tags=[]
    )


    def delete(self, request, pk):
        try:
            location = Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            return Response({"error": "LOcation not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if location.created_by != request.user:
            return Response(
                {"error": "You do not have permission to delete this center."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        location.delete()
        return Response({"message": "Markaz muvaffaqiyatli ochirildi."}, status=status.HTTP_204_NO_CONTENT)
