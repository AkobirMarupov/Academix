from rest_framework.urls import path

from .create.views import GroupStudetCreateAPIView
from .delete.views import GroupStudentDeleteAPIView
from .list.views import GroupStudentListAPIView, GroupStudentRetriewAPIView
from .update.views import GrioupStudentUpdateAPIView


urlpatterns = [
    path('list/', GroupStudentListAPIView.as_view(), name='groups-list'),
    path('create/', GroupStudetCreateAPIView.as_view(), name='groups-create'),
    path('<int:pk>/detail/', GroupStudentRetriewAPIView.as_view(), name='groups-retriev'),
    path('<int:pk>/update/', GrioupStudentUpdateAPIView.as_view(), name='groups-update'),
    path('<int:pk>/delete/', GroupStudentDeleteAPIView.as_view(), name='groups-delete'),
]