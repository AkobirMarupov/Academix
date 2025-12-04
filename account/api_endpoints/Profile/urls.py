from rest_framework.urls import path

from .create.views import ProfileCreateAPIView
from .list.views import ProfileListAPIView, ProfileRetriewAPIView
from .delete.views import ProfileDeleteAPIView
from .update.views import ProfileUpdateAPIView



urlpatterns = [
    path('<int:pk>/', ProfileRetriewAPIView.as_view(), name='profile-retriev'),
    path('update/<int:pk>/', ProfileUpdateAPIView.as_view(), name="profile-update"),
    path('list/', ProfileListAPIView.as_view(), name="profile-list"),
    path('create/', ProfileCreateAPIView.as_view(), name='profile-create'),
    path('delete/<int:pk>/', ProfileDeleteAPIView.as_view(), name='profile-delete')
]
