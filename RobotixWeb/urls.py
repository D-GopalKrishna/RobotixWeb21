""" RobotixWeb URL Configuration """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

schema_view = get_schema_view(
   openapi.Info(
      title="Robotix Web API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="unijay12@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),

    #apps urls
    path('api/users/', include('users.urls'), name="users"),
    path('api/about/', include('about.urls'), name="about"),
    path('api/certificate/', include('certificate.urls'), name="certificate"),
    path('api/events/', include('events.urls'), name="events"),
    path('api/extras/', include('extras.urls'), name="extras"),
    # path('api/roboexpo/', include('roboexpo.urls'), name="roboexpo"),
    # path('api/roboPortal/', include('roboPortal.urls'), name="roboPortal"),
   #  path('api/workshops/', include('roboPortal.urls'), name="roboPortal"),
    path('api/recruitment/', include('recruitment.urls'), name="recruitment"),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)