from django.urls import path
from center.api_endpoints.center.create.views import CenterCreateAPIView

urlpatterns = [
    path('centers/create/', CenterCreateAPIView.as_view(), name='center-create'),
]
