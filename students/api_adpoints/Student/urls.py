from django.urls import path
from .list.views import StudentListAPIView, StudentRetrievAPIView
from .create.views import StudentCreateAPIView
from .delete.views import StudentDeleteAPIView
from .update.views import StudentUpdateAPIView

urlpatterns = [
    path('list/', StudentListAPIView.as_view(), name='student-list'),
    path('create/', StudentCreateAPIView.as_view(), name='student-create'),
    path('<int:pk>/detail/', StudentRetrievAPIView.as_view(), name='student-retriev'),
    path('<int:pk>/update/', StudentUpdateAPIView.as_view(), name='student-update'),
    path('<int:pk>/delete/', StudentDeleteAPIView.as_view(), name='student-delete'),
]
