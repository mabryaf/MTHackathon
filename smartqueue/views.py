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
    HTTP_200_OK
)
# from rest_framework.parsers import JSONParser, ParseError

from . import models
from . import serializers
from . import smartqueue
from . import tests

import json
import requests

from random import randrange # to simulate occupancy sensor and queue times
import random #simulate the assignment of addresses
import unittest
import uuid # unique IDs for queues
import arrow # advanced date data types
from enum import Enum # for reservation states

sq = smartqueue.SmartQueue(smartqueue.testqueue_schedule)

# 5. User --> id(p.k) ????
class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

# 3. Location --> address(p.k), max_capacity, queues(f.k)?
class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer

# 4. Resource --> id(p.k), capacity, __occupant_sensor
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer

# 2. Queue --> id(p.k), open_datetime, close_datetime, max_capacity, address, resource_id(f.k), reservations list? -- one to many relation with class Reservation.
class QueueViewSet(viewsets.ModelViewSet):
    queryset = models.Queue.objects.all()
    serializer_class = serializers.QueueSerializer

# 1. Reservation --> id(p.k), person_id?, state, reward_points
# class ReservationViewSet(viewsets.ModelViewSet):
#     queryset = models.Reservation.objects.all()
#     serializer_class = serializers.ReservationSerializer

# class Reservation:
#   def user(self, person_id, reward_points):
#     self.id = uuid.uuid1()
#     self.person_id = person_id
#     self.state = ReservationState.RESERVED
#     self.reward_points = reward_points
  
#   def update(self, new_state):
#     self.state = new_state

# class Customer(self, name):
#     def __init__(self, name, max_capacity):
#         self.name = name

#     def get_name(self):
#         return self.name

# Create your views here.

@api_view(['GET'])
def home(request):
    customers = models.Person.objects.all()
    # test = smartqueue_v0_3.SmartQueue(smartqueue_v0_3.queue_schedule)
    # print(test.list_queue_options("resource1", "address1", arrow.get('2020-07-06 13:00', 'YYYY-MM-DD HH:mm'), arrow.get('2020-07-06 13:10', 'YYYY-MM-DD HH:mm')))
    # print("ENDOFLINE")
    # print(customers)
    # for customer in customers:
    #     print(customer)

    # print(a.get_name())
    print(sq.list_reservations("abc123"))
    sq.update(smartqueue.testqueue_schedule)
    # sq._SmartQueue__resource
    for resource in sq._SmartQueue__resources:
        print(resource.id)
    
    return Response({"Connected to db private"}, status=HTTP_200_OK)

@api_view(['GET'])
def users(request):
    results = serializers.UserSerializer(tests.users, many=True).data
    return Response(results)

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

    #reserve
    queue_id = ''
    for queue in sq._SmartQueue__queues:
        queue_id = queue.id
    print(queue_id)
    reserved = sq.reserve(person_id, "", 1, queue_id)
    print(reserved)

    reservations = sq.list_reservations(person_id)
    for reservation in reservations:
        reservation['reservation_state'] = str(reservation['reservation_state'])
        reservation['start_time'] = str(reservation['start_time'])
        reservation['end_time'] = str(reservation['end_time'])

    return JsonResponse(reservations, safe=False)

@api_view(['POST'])
def reserve(request):
    person_id = request.data.get("person_id")
    proof_of_purchase = request.data.get("proof_of_purchase")
    occupants = request.data.get("occupants")

    #reserve
    queue_id = ''
    for queue in sq._SmartQueue__queues:
        queue_id = queue.id
    print(queue_id)
    reserved = sq.reserve(person_id, "", 1, queue_id)
    print(reserved)

    return Response({'token'})

