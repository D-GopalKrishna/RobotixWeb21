from rest_framework import serializers, viewsets
from .models import *

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


