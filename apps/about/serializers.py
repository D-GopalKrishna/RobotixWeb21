from rest_framework import serializers,viewsets
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievements
        fields = '__all__'

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['get']