from django.urls import path

from .create.views import TeacherCreateAPIView
from .list.views import TeacherListAPIView, TeacherRetriveAPIView
from .delete.views import TeacherDeleteAPIView
from .update.views import TeacherUpdateAPIView

urlpatterns = [
    path('list/', TeacherListAPIView.as_view(), name='teacher-list'),
    path('retriev/<int:pk>/', TeacherRetriveAPIView.as_view(), name='teacher-retriev'),
    path('create/', TeacherCreateAPIView.as_view(), name='teacher-create'),
    path('update/<int:pk>/', TeacherUpdateAPIView.as_view(), name='teacher-update'),
    path('delete/<int:pk>/', TeacherDeleteAPIView.as_view(), name='teacher-delete')
]