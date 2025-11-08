from rest_framework.urls import path
from .create.views import CourseCreateAPIView
from .update.views import CourseUpdateAPIView
from .list.views import CourseListAPIView, CourseRetrievAPIView
from .delete.views import CourseDeleteAPIView


urlpatterns = [
    path('<int:pk>/', CourseRetrievAPIView.as_view(), name='course-retriev'),
    path('update/<int:pk>/', CourseUpdateAPIView.as_view(), name="course-update"),
    path('list/', CourseListAPIView.as_view(), name="course-list"),
    path('create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('delete/<int:pk>/', CourseDeleteAPIView.as_view(), name='course-delete')
]