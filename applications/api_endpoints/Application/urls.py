from django.urls import path
from .confirmation.views import (
    ApplicationListAPIView,
    MyApplicationsAPIView,
    ApplicationApproveRejectAPIView,
    ApplicationNotificationsAPIView
)

urlpatterns = [
    path('applications/', ApplicationListAPIView.as_view(), name='applications-list'),
    path('applications/<int:pk>/confirm/', ApplicationApproveRejectAPIView.as_view(), name='application-confirm'),

    path('my-applications/', MyApplicationsAPIView.as_view(), name='my-applications'),
    path('notifications/', ApplicationNotificationsAPIView.as_view(), name='application-notifications'),
]
