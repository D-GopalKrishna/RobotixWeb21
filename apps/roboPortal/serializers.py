from rest_framework import serializers, viewsets
from .models import portalUser,Team
from allauth.account.adapter import get_adapter
from rest_auth.registration import serializers as RegisterSerializer
from roboPortal.models import portalUser, Team, Robothon
from users.serializers import UserProfileSerializer, UserDetailsTeamSerializer



class PortalUserSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = portalUser
        fields = ('user','joined_team')


class Teamserializer(serializers.ModelSerializer):
    admin = UserDetailsTeamSerializer(read_only=True)
    member = UserDetailsTeamSerializer(read_only=True,many=True)

    class Meta:
        model = Team
        fields = ('name','admin','member')


class RobothonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robothon
        fields = '__all__'


## _________________ Viewsets ____________________________


class PortalUserViewSet(viewsets.ModelViewSet):
    queryset = portalUser.objects.all()
    serializer_class = PortalUserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = Teamserializer


class RobothonViewSet(viewsets.ModelViewSet):
    queryset = Robothon.objects.all()
    serializer_class = RobothonSerializer
