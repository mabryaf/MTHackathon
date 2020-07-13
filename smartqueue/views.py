from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from django.http import JsonResponse

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
from . import smartqueue_v0_3

import json
import requests

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
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer

class Reservation:
  def user(self, person_id, reward_points):
    self.id = uuid.uuid1()
    self.person_id = person_id
    self.state = ReservationState.RESERVED
    self.reward_points = reward_points
  
  def update(self, new_state):
    self.state = new_state

# Create your views here.
@api_view(['GET'])
def home(request):
    a = models.Person.objects.get(name='mabry')
    print(models.Person.objects.get_name())
    print(a.get_name())
    return Response({"Connected to db private"}, status=HTTP_200_OK)