from rest_framework.urls import path
from .create.views import HomeworkCreateAPIView
from .update.views import HomeworkUpdateAPIView


urlpatterns = [
    path('update/<int:pk>/', HomeworkUpdateAPIView.as_view(), name="course-update"),
    path('create/', HomeworkCreateAPIView.as_view(), name='course-create'),
]