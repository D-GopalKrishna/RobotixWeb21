from rest_framework import serializers, viewsets
from .models import *


class DIY_FYISerializer(serializers.ModelSerializer):
    class Meta:
        model = DIY_FYI
        fields = "__all__"


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = '__all__'


class SponserViewSet(viewsets.ModelViewSet):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorSerializer
    http_method_names = ['get']


class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web
        fields = "__all__"


class WebViewSet(viewsets.ModelViewSet):
    queryset = DIY_FYI.objects.all()
    serializer_class = DIY_FYISerializer
    http_method_names = ['get']


class GallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gallery
        fields = "__all__"

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    http_method_names = ['get']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class ContactViewset(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    http_method_names = ['get']