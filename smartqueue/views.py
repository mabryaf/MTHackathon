from django.shortcuts import render

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg

from rest_framework import pagination
from rest_framework import viewsets, mixins
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
# from rest_framework.parsers import JSONParser, ParseError

from . import models
from . import serializers

import json

from rest_framework import filters
import requests
from google.transit import gtfs_realtime_pb2
from google.protobuf import json_format
from django.http import JsonResponse


# from gtfspy import TransitData

# http://datamine.mta.info/mta_esi.php?key=0573425b4f41d266e0c12a4275c92ec1

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

# Create your views here.
@api_view(['GET'])
def home(request):
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get("http://datamine.mta.info/mta_esi.php?key=0573425b4f41d266e0c12a4275c92ec1", allow_redirects=True)
    feed.ParseFromString(response.content)
    # test = json.dumps(str(feed.entity), default=set_default)
    test = json_format.MessageToJson(feed)
    # with open('json_filename', 'w') as f:
    #         f.write(test)

    # json_data = open('json_filename')   
    # data1 = json.load(json_data) # deserialises it
    # data2 = json.dumps(data1) # json formatted string
    # json_data.close()

    # print(test)
    print(feed.entity[1])


    return Response({"Connected to db private"}, status=HTTP_200_OK)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

