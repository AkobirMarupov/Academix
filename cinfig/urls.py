from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Shop_Stack API",
      default_version='v1',
      description="ShopStack platform API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('i18n/', include('django.conf.urls.i18n')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('👤Account/', include('account.urls')),
    path('📌Profile/', include('account.api_endpoints.Profile.urls')),
    path('🏛Center/', include("center.api_endpoints.center.urls")),
    path('👨🏼‍🏫Teacher/', include("center.api_endpoints.teacher.urls")),
    path('📍Location/', include("center.api_endpoints.location.urls")),
    path('📚Course/', include('course.api_endpoints.course.urls')),
    path('🥇Review/', include('course.api_endpoints.review.urls')),
    path('🎒homework/', include('course.api_endpoints.homework.urls')),
    path('👨‍🎓Student/', include('students.api_adpoints.Student.urls')),
    path('👥Groups/', include('groups.api_endpoints.group.urls')),
    path('👫GroupStudent/', include('groups.api_endpoints.groupstudent.urls')),
    path('📜Applications/', include('applications.api_endpoints.Application.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
