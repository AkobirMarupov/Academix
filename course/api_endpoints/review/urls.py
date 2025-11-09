from django.urls import path
from .create.views import ReviewCreateAPIView
from .delete.views import ReviewDeleteAPIView
from .list.views import ReviewListAPIView, ReviewRetrieveAPIView
from .update.views import ReviewUpdateAPIView

urlpatterns = [
    path('<int:pk>/', ReviewRetrieveAPIView.as_view(), name='review-retriev'),
    path('update/<int:pk>/', ReviewUpdateAPIView.as_view(), name="review-update"),
    path('list/', ReviewListAPIView.as_view(), name="review-list"),
    path('create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('delete/<int:pk>/', ReviewDeleteAPIView.as_view(), name='review-delete')
]
