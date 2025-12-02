from rest_framework.urls import path

from .create.views import GroupCreateAPIView
from .update.views import GrioupUpdateAPIView
from .list.views import GroupListAPIView, GroupRetriewAPIView
from .delete.views import GroupDeleteAPIView


urlpatterns = [
    path('list/', GroupListAPIView.as_view(), name='group-list'),
    path('create/', GroupCreateAPIView.as_view(), name='group-create'),
    path('<int:pk>/detail/', GroupRetriewAPIView.as_view(), name='group-retriev'),
    path('<int:pk>/update/', GrioupUpdateAPIView.as_view(), name='group-update'),
    path('<int:pk>/delete/', GroupDeleteAPIView.as_view(), name='group-delete'),
]