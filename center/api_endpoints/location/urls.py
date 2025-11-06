from django.urls import path
from .create.views import LocationCreateAPIView
from .list.views import LocationListAPIView, LocationRetrievAPIView
from .update.views import LOcationUPdateAPIView
from .delete.views import LocatinDeleteAPIView

urlpatterns = [
    path('list/', LocationListAPIView.as_view(), name='location-list'),  
    path('<int:pk>/', LocationRetrievAPIView.as_view(), name='location-retrieve'),  
    path('create/', LocationCreateAPIView.as_view(), name='location-create'), 
    path('update/<int:pk>/', LOcationUPdateAPIView.as_view(), name='location-update'),  
    path('delete/<int:pk>/', LocatinDeleteAPIView.as_view(), name='location-delete'),  
]

