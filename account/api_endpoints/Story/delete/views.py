from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from account.models import Story



class StoryDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            story = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Response({'detail': 'Bunday Story topilmadi.'}, status=status.HTTP_403_FORBIDDEN)
        
        
        story.delete()
        return Response({"message": "Story muvaffaqiyatli ochirildi."})