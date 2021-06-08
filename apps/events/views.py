from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
import datetime

# Create your views here.

now_time = datetime.datetime.now().strftime("%Y-%m-%d")


@api_view()
def event_api(request):
    obj_event = Event.objects.all()
    serializer1 = EventSerializer(obj_event,many=True)
    dict = {'Event':serializer1.data}

    return Response(dict)


@api_view()
def year_event_api(request):
    obj_event = Event.objects.filter(date_time__year=str(now_time[0:4]))
    year_data_serializer = EventSerializer(obj_event,many=True)
    print(year_data_serializer)
    dict = {'YearEvent':year_data_serializer.data}

    return Response(dict)
