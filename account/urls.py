from django.urls import path

from account.api_endpoints.Profile.Verify.views import RegisterUserAPIView, RegisterConfirmAPIView


urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register-user'),
    path('register/confirm/', RegisterConfirmAPIView.as_view(), name='register-confirm'),
]