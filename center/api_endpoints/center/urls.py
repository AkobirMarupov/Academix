from django.urls import path
from .create.views import CenterCreateAPIView
from .list.views import CenterLIstAPIView, CenterRetrieveAPIView
from .update.views import CenterUpdateAPIView
from .delete.views import CenterDEleteAPIView

urlpatterns = [
    path('<int:pk>/', CenterRetrieveAPIView.as_view(), name='center-retriev'),
    path('update/<int:pk>/', CenterUpdateAPIView.as_view(), name="center-update"),
    path('list/', CenterLIstAPIView.as_view(), name="center-list"),
    path('create/', CenterCreateAPIView.as_view(), name='center-create'),
    path('delete/<int:pk>/', CenterDEleteAPIView.as_view(), name='center-delete')

    
]
