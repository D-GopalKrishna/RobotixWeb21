from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.


class About(APIView):

    def get(self,request,*args, **kwargs):
        Alumini = Team.objects.filter(post_assign="AA").all()
        Convenor = Team.objects.filter(post_assign="CC").all()
        Manager = Team.objects.filter(post_assign="MM").all()
        HeadCoordinator = Team.objects.filter(post_assign="HC").all()
        Coordinator = Team.objects.filter(post_assign="CO").all()
        Volunteer = Team.objects.filter(post_assign="VO").all()

        serializer1 = TeamSerializer(Alumini , many=True)
        serializer2 = TeamSerializer(Convenor, many=True)
        serializer3 = TeamSerializer(Manager,many=True)
        serializer4 = TeamSerializer(HeadCoordinator,many=True)
        serializer5 = TeamSerializer(Coordinator,many=True)
        serializer6 = TeamSerializer(Volunteer,many=True)

        dict = {'Alumini' : serializer1.data ,'Convenor' : serializer2.data ,'Manager' : serializer3.data, 'HeadCoordinator' : serializer4.data, 'Coordinator' : serializer5.data, 'Volunteer' : serializer6.data }

        return Response(dict)