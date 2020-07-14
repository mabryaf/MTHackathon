from django.db import models
from django.contrib.postgres.fields import ArrayField

from random import randrange # to simulate occupancy sensor and queue times
import random #simulate the assignment of addresses
import unittest
import uuid # unique IDs for queues
import arrow # advanced date data types
from enum import IntEnum # for reservation states

# def ranges_overlap(r1_start, r1_end, r2_start, r2_end):
#   starts_overlap = (r1_start >= r2_start) and (r1_start <= r2_end)
#   ends_overlap = (r1_end >= r2_start) and (r1_end <= r2_end)
#   r1_is_a_superset = (r1_start <= r2_start) and (r1_end >= r2_end)

#   ranges_overlap = starts_overlap or ends_overlap or r1_is_a_superset
#   return ranges_overlap

# # 5. User --> id(p.k) ????
# class PersonManager(models.Manager):
#     def get_name(self):
#         return self.name
class Person(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #not usable if not postgres
    name = models.CharField(max_length=63)
    def get_name(self):
        return self.name

# class LocationManager(models.Manager):
#     def remaining_capacity(self, start_datetime, end_datetime):
#         occupants_scheduled_to_be_at_location = 0
#         for queue in self.queue_set:
#             queue_in_range = ranges_overlap(start_datetime, end_datetime, queue.open_datetime, queue.close_datetime)

#         if queue_in_range:
#             occupants_scheduled_to_be_at_location += queue.active_occupants()
        
#         return self.max_capacity - occupants_scheduled_to_be_at_location
# # 3. Location --> address(p.k), max_capacity, queues(f.k)?
class Location(models.Model):
    address = models.CharField(max_length=63)
    max_capacity = models.IntegerField()

# class ResourceManager(models.Manager):
#     def occupants(self):
#         return self.occupant_sensor()
#     def remaining_capacity(self):
#         return self.capacity - self.occupant_sensor()

# # 4. Resource --> id(p.k), capacity, __occupant_sensor
class Resource(models.Model):
    capacity = models.IntegerField()
    occupant_sensor = models.IntegerField()

# 2. Queue --> id(p.k), open_datetime, close_datetime, max_capacity, address, resource_id(f.k), reservations list? -- one to many relation with class Reservation.
class Queue(models.Model):
    open_datetime = models.DateTimeField(max_length=15, null = True)
    close_datetime = models.DateTimeField(max_length=15, null = True)
    max_capacity = models.IntegerField()
    address = models.CharField(max_length=63)
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class ReservationState(IntEnum):
    RESERVED = 1
    CANCELED = 2
    MISSED = 3
    COMPLETED = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class ReservationManager(models.Manager):
    def update(self, new_state):
        self.state = new_state
# 1. Reservation --> id(p.k), person_id?, state, reward_points
class Reservation(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    state = models.IntegerField()
    reward_points = models.IntegerField()
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)