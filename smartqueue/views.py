from django.http import JsonResponse, HttpResponse

from rest_framework import viewsets, mixins, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)

from . import models
from . import serializers
from . import smartqueue
from . import tests

from .smartqueue import sq

import json
import requests
# import datetime
import random #simulate the assignment of addresses
import unittest
import uuid # unique IDs for queues
import arrow # advanced date data types

from random import randrange # to simulate occupancy sensor and queue times
from enum import Enum # for reservation states
from datetime import datetime

#instantiate smartqueue
###Check if the update() is persistent
# sq = smartqueue.SmartQueue(smartqueue.test2)
# for queue in sq._SmartQueue__queues:
#     user = random.choice(tests.users)["person_id"]
#     resered = sq.reserve("e973d77cc5c911eaa2ba0242ac100002", "", 1, queue.id)
    # print (queue.id, user)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer

class QueueViewSet(viewsets.ModelViewSet):
    queryset = models.Queue.objects.all()
    serializer_class = serializers.QueueSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer
    
@api_view(['POST'])
def reservations(request):
    #Get posted data from JSON request
    person_id = request.data.get("person_id")

    #add one reservation for user 1
    queue_id = ''
    for queue in sq._SmartQueue__queues:
        queue_id = queue.id
    sq.reserve("e973d45cc5c911eaa2ba0242ac100002", "", 1, queue_id)
    
    #list the reservations
    reservations = sq.list_reservations(person_id)
    print(reservations, person_id)
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
    #Get posted data from JSON request
    person_id = request.data.get("person_id")
    proof_of_purchase = request.data.get("proof_of_purchase")
    occupants = request.data.get("occupants")
    queue_id = request.data.get("queue_id")

    #execute reservation
    result = sq.reserve(person_id, proof_of_purchase, occupants, queue_id)
    
    #update reward points
    if result['code'] == smartqueue.ReserveActionResult.SUCCESS:
        queryset = models.Customer.objects.filter(person_id=person_id)
        for n in queryset:
            n.reward_points += result['reward_points']
            queryset.update()

    # return Response({'Your reservation has been made'})
    return JsonResponse(result['reward_points'], safe=False)

@api_view(['POST'])
def cancel_reservation(request):
    #Get posted data from JSON request
    queue_id = request.data.get("queue_id")
    person_id = request.data.get("person_id")

    #execute cancellation
    result = sq.cancel_reservation(queue_id, person_id)

    return Response({'Cancelled'})
    # return JsonResponse(result, safe=False)

@api_view(['POST'])
def complete_reservation(request):
    #Get posted data from JSON request
    queue_id = request.data.get("queue_id")
    person_id = request.data.get("person_id")

    #execute cancellation
    result = sq.complete_reservation(queue_id, person_id)

    return Response({'Completed'})
    # return JsonResponse(result, safe=False)

@api_view(['POST'])
def search(request):
    #Get posted data from JSON request
    location1 = request.data.get("location1")
    location2 = request.data.get("location2")
    date = request.data.get("date")
    time = request.data.get("time")
    bestqueue = request.data.get("bestqueue")

    # location1 = 51, POUGHKEEPSIE
    # location2 = 1, GRAND CENTRAL
    # date = 2020/07/15
    # time = 1354

    #Create url api for stations
    url = "https://mnorthstg.prod.acquia-sites.com/wse/trains/v4/"+location1+"/"+location2+"/DepartBy/"+date+"/"+time+"/9de8f3b1-1701-4229-8ebc-346914043f4a/Tripstatus.json"
    test = "https://mnorthstg.prod.acquia-sites.com/wse/trains/v4/51/1/DepartBy/2020/07/15/1354/9de8f3b1-1701-4229-8ebc-346914043f4a/Tripstatus.json"

    #Retrieve json from api
    r = requests.get(test)
    r = json.loads(r.text)

    #Retrieve details of interest in api
    resource_list = []
    for x in r["GetTripStatusJsonResult"]:
        # origintime = x["OriginDateTime"]
        # otime = origintime[:10]+" "+origintime[11:16]
        # destinationtime = x["DestinationDateTime"]
        # dtime = destinationtime[:10]+" "+destinationtime[11:16]
        # resource_list.append((int(x["TrainName"]), x["Origin"], otime, dtime))
        resource_list.append((int(x["TrainName"])))

    print(resource_list)
    # for queue in sq._SmartQueue__queues:
    #     print(queue.id)
    # for resource in sq._SmartQueue__resources:
    #     print(resource.id)    
    # for location in sq._SmartQueue__locations:
    #     print(location.address)

    # a = "2020-07-15T15:20:44:00"
    

    # if arrow.get() >= arrow.get('2020-07-15 13:00'):
    #     print(True)
    # sample = sq.list_queue_options(8840, "POUGHKEEPSIE", '2020-07-06 13:00', '2020-07-16 13:20')
    # working sample
    sample = sq.list_queue_options(8815, "Grand Central", '2020-07-06 13:00', '2020-07-16 13:20')

    
    for s in sample:
        s['start_time'] = s['start_time'].format('YYYY-MM-DD HH:mm')
        s['end_time'] = s['start_time'].format('YYYY-MM-DD HH:mm')
    
    # #Create list that will be processed by smartqueue
    final_list = []
    for n in resource_list:
        options = sq.list_queue_options(n[0], n[1], n[2], n[3])
        final_list.append(options)

    print(sample)
    print(final_list)
    # return JsonResponse(final_list, safe=False)
    return JsonResponse(sample, safe=False)

@api_view(['GET'])
def test(request):
    r = requests.get("https://smartqueueapi.azurewebsites.net/resource/")
    r = json.loads(r.text)
    sq.update(r)
    return Response({'Welcome to Smartqueue API'})

    # qs_json = serialize('json', queryset)
    # print(qs_json)

    # def get_queryset(self):
    #     queryset = models.Resource.objects.all()
    #     for query in queryset.all():
    #         for location in query.locations.all():
    #             print(location.address_id)
    #     return queryset
    # def list(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # queryset = models.Resource.objects.all()
    # data = list(queryset.values("locations"))
    # return JsonResponse(data, safe=False)

    # results = models.Resource.objects.values('id', 'resource_id','train_from','train_to','max_occupancy','occupancy_sensor','updated_date','locations')
    # print(list(results))

@api_view(['GET'])
def testing(request):
    queuelist = []
    for queue in sq._SmartQueue__queues:
        queuelist.append(queue.id)
        # print(queue.id)
    return JsonResponse(queuelist, safe=False)


