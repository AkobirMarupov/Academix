from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from account.models import Profile



class ProfileDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({'detail': 'Bunday profile topilmadi.'}, status=status.HTTP_403_FORBIDDEN)
        
        
        profile.delete()
        return Response({"message": "Profile muvaffaqiyatli ochirildi."}, status=status.HTTP_204_NO_CONTENT)