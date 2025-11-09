from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from course.models import Review
from course.api_endpoints.review.create.serializers import ReviewCreateSerializers


class ReviewCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create a new Center",
        request_body=ReviewCreateSerializers,
        responses={
            201: openapi.Response(
                description="Center created successfully",
                schema=ReviewCreateSerializers()
            ),
            400: "Notugri malumot yuborildi",
            401: "Avtorizatsiya talab etiladi",
        },
        tags=[],
    )

    def post(self, request):
        serializer = ReviewCreateSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(created_at = request.user)
            return Response(
                {'detail': 'Malumot muvaffaqiyatli yaratildi.', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)