from django.urls import path, include
from rest_framework import routers
from .serializers import *
from .views import *

router = routers.DefaultRouter()
router.register(r'sponsors', SponserViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'web', WebViewSet)
router.register(r'Contact', ContactViewset)

app_name = 'info'

urlpatterns = [
    path('',include(router.urls)),
    path('docs/',DIYFYI.as_view())
]
