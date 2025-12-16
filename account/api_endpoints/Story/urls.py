from rest_framework.urls import path

from .create.views import StoryCreateAPIView
from .list.views import StoryListAPIView, StoryRetriewAPIView
from .delete.views import StoryDeleteAPIView
from .update.views import StoryUpdateAPIView



urlpatterns = [
    path('<int:pk>/', StoryRetriewAPIView.as_view(), name='story-retriev'),
    path('update/<int:pk>/', StoryUpdateAPIView.as_view(), name="story-update"),
    path('list/', StoryListAPIView.as_view(), name="story-list"),
    path('create/', StoryCreateAPIView.as_view(), name='story-create'),
    path('delete/<int:pk>/', StoryDeleteAPIView.as_view(), name='story-delete')
]
