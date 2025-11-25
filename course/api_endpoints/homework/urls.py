from rest_framework.urls import path
from .create.views import HomeworkCreateAPIView
from .update.views import HomeworkUpdateAPIView
from .delete.views import HomeworkDeleteAPIView
from .list.views import HomeworkListAPIView, HomeworkRetrievAPIView


urlpatterns = [
    path('<int:pk>/', HomeworkRetrievAPIView.as_view(), name='homework-retriev'),
    path('update/<int:pk>/', HomeworkUpdateAPIView.as_view(), name="homework-update"),
    path('list/', HomeworkListAPIView.as_view(), name="homework-list"),
    path('create/', HomeworkCreateAPIView.as_view(), name='homework-create'),
    path('delete/<int:pk>/', HomeworkDeleteAPIView.as_view(), name='homework-delete'),
]