
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from applications.models import Application, ApplicationStatusNotification
from applications.api_endpoints.Application.confirmation.serializers import ApplicationConfirmationSerializer



class ApplicationApproveRejectAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            application = Application.objects.get(id=pk)
        except Application.DoesNotExist:
            return Response({"detail": "Ariza topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ApplicationConfirmationSerializer(application, data=request.data, partial=True)
        if serializer.is_valid():
            new_status = serializer.validated_data.get("status")

            if new_status not in ["approved", "rejected"]:
                return Response(
                    {"detail": "Status faqat 'approved' yoki 'rejected' bo‘lishi mumkin."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save()

            ApplicationStatusNotification.objects.create(
                application=application,
                message=f"Arizangiz '{application.course.name}' kursi uchun {application.get_status_display()} holatiga o‘zgartirildi."
            )

            return Response(
                {
                    "message": f"Ariza {new_status} qilindi.",
                    "application": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
