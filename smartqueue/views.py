from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from django.http import JsonResponse, HttpResponse

from rest_framework import pagination, viewsets, mixins, filters
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework import status
# from rest_framework.parsers import JSONParser, ParseError

from . import models
from . import serializers
from . import smartqueue
from . import tests

from django.http import JsonResponse


import json
import requests
import datetime
import random

from random import randrange # to simulate occupancy sensor and queue times
import random #simulate the assignment of addresses
import unittest
import uuid # unique IDs for queues
import arrow # advanced date data types
from enum import Enum # for reservation states
from django.http import JsonResponse


sq = smartqueue.SmartQueue(smartqueue.test2)
# for queue in sq._SmartQueue__queues:
#     user = random.choice(tests.users)["person_id"]
#     resered = sq.reserve("e973d77cc5c911eaa2ba0242ac100002", "", 1, queue.id)
    # print (queue.id, user)

# 3. Location --> address(p.k), max_capacity, queues(f.k)?
class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer

# 4. Resource --> id(p.k), capacity, __occupant_sensor
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer

    # results = models.Resource.objects.values('id', 'resource_id','train_from','train_to','max_occupancy','occupancy_sensor','updated_date','locations')
    # print(list(results))

# 2. Queue --> id(p.k), open_datetime, close_datetime, max_capacity, address, resource_id(f.k), reservations list? -- one to many relation with class Reservation.
class QueueViewSet(viewsets.ModelViewSet):
    queryset = models.Queue.objects.all()
    serializer_class = serializers.QueueSerializer

# @api_view(['GET'])
def users(request):
#     queue_id = ''
#     for queue in sq._SmartQueue__queues:
#         queue_id = queue.id
#         user = random.choice(tests.users)["person_id"]
#         sq.reserve("e973d77cc5c911eaa2ba0242ac100002", "", 1, queue_id)
    return Response("")

# class CustomerViewSet(viewsets.ViewSet):
#     # Required for the Browsable API renderer to have a nice form.
#     serializer_class = serializers.UserSerializer

#     def list(self, request):
#         serializer = serializers.UserSerializer(
#             instance=tasks.values(), many=True)
#     return Response(serializer.data)

class CustomerViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.CustomerSerializer

    def list(self, request):
        serializer = serializers.CustomerSerializer(
            instance=tests.customers.values(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        pk = ''
        name = ''
        reward_points = 100
        for x in tests.customers.values():
            if x.person_id == kwargs['pk']:
                pk = x.person_id
                name = x.name
                reward_points = x.reward_points
        return Response({"pk": pk, "name": name, "reward_points": reward_points})

@api_view(['POST'])
def reservations(request):
    person_id = request.data.get("person_id")

    queue_id = ''
    for queue in sq._SmartQueue__queues:
        queue_id = queue.id
        print(queue_id)
    reserved = sq.reserve("abc_123", "", 1, queue_id)
    
    reservations = sq.list_reservations(person_id)
    for reservation in reservations:
        reservation['reservation_state'] = str(reservation['reservation_state'])
        reservation['start_time'] = str(reservation['start_time'])
        reservation['end_time'] = str(reservation['end_time'])
        queryset = models.Resource.objects.filter(resource_id=reservation["resource"])
        for query in queryset:
            reservation["train_from"]= query.train_from
            reservation["train_to"]= query.train_to

    return JsonResponse(reservations, safe=False)

@api_view(['POST'])
def reserve(request):
    person_id = request.data.get("person_id")
    proof_of_purchase = request.data.get("proof_of_purchase")
    occupants = request.data.get("occupants")
    queue_id = request.data.get("queue_id")

    return Response({'Your reservation has been made'})

@api_view(['POST'])
def cancel_reservation(request):
    queue_id = request.data.get("queue_id")
    person_id = request.data.get("person_id")

    # sq.cancel_reservation(queue_id, person_id)

    return Response({'Your reservation has been cancelled'})

@api_view(['POST'])
def search(request):
    location1 = request.data.get("location1")
    #give location/location name, then i can get resource_id
    location2 = request.data.get("location2")
    date = request.data.get("date")
    time = request.data.get("time")
    bestqueue = request.data.get("bestqueue")

    #make db query based on post data
    #now i have train names

    #def list_queue_options(self, resource_id, address, start_datetime, end_datetime):
    # get resource names, train departure, train occupancy, queue occupancy, route_points
    # sort via nearest time, then sort via descending route points

    return Response({'request'})


