from rest_framework import generics, permissions
from applications.models import Application
from .serializers import ApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from applications.models import Application, ApplicationStatusNotification
from .serializers import ApplicationConfirmationSerializer, ApplicationStatusNotificationSerializer



class ApplicationListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Application.objects.all().order_by('-submitted_at')
    serializer_class = ApplicationSerializer


class MyApplicationsAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Application.objects.filter(student=self.request.user).order_by('-submitted_at')
    
    serializer_class = ApplicationSerializer




class ApplicationApproveRejectAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, pk):
        try:
            application = Application.objects.get(id=pk)
        except Application.DoesNotExist:
            return Response({"detail": "Ariza topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ApplicationConfirmationSerializer(application, data=request.data, partial=True)
        if serializer.is_valid():
            new_status = serializer.validated_data.get("status")
            comment = serializer.validated_data.get("comment", "")

            if new_status not in [Application.STATUS_APPROVED, Application.STATUS_REJECTED]:
                return Response({"detail": "Status faqat 'approved' yoki 'rejected' bo‘lishi mumkin."}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            ApplicationStatusNotification.objects.create(
                application=application,
                message=comment or f"Ariza {new_status} holatiga o‘zgartirildi.",
                status=new_status
            )

            return Response({"message": f"Ariza '{new_status}' holatiga o‘zgartirildi.", "application": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ApplicationNotificationsAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ApplicationStatusNotificationSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return ApplicationStatusNotification.objects.all().order_by('-status_changed_at')

        return ApplicationStatusNotification.objects.filter(application__student=self.request.user).order_by('-status_changed_at')
