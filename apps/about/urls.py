
from django.urls import path,include
from .views import *
from rest_framework import routers
from .serializers import AchievementViewSet

router = routers.DefaultRouter()
router.register(r'achievement', AchievementViewSet)

urlpatterns = [
    path('team/',About.as_view(),name='text'),
    path('',include(router.urls),name='about_api')
]
