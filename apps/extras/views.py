from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.


class DIYFYI(APIView):

    def get(self,request,*args, **kwargs):
        diy = DIY_FYI.objects.filter(link='').all()
        fiy = DIY_FYI.objects.filter(file='').all()
        serializer1 = DIY_FYISerializer(diy , many=True)
        serializer2 = DIY_FYISerializer(fiy, many=True)
        

        dict = {'DIY' : serializer1.data ,'FYI' : serializer2.data  }

        return Response(dict)