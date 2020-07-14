from . import models
from rest_framework import serializers

# 5. User --> id(p.k) ????
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'name']

# 3. Location --> address(p.k), max_capacity, queues(f.k)?
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ['id', 'address', 'max_capacity']

# 4. Resource --> id(p.k), capacity, __occupant_sensor
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        fields = ['id', 'capacity', 'occupant_sensor']

# 2. Queue --> id(p.k), open_datetime, close_datetime, max_capacity, address, resource_id(f.k), reservations list? -- one to many relation with class Reservation.
class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Queue
        fields = ['id', 'open_datetime', 'close_datetime', 'max_capacity', 'address', 'resource_id', 'location']

# 1. Reservation --> id(p.k), person_id?, state, reward_points
# class ReservationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Reservation
#         fields = ['id', 'person_id', 'state', 'reward_points', 'queue']

class UserSerializer(serializers.Serializer):
    person_id = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)

class CustomerSerializer(serializers.Serializer):
    person_id = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=256)
    reward_points = serializers.IntegerField()

class ReservationSerializer(serializers.Serializer):
    # id = serializers.CharField(max_length=200)
    # person_id = serializers.CharField(max_length=200)
    # state = serializers.CharField(max_length=200)
    # reward_points = serializers.IntegerField()
    # occupants = serializers.IntegerField()
    fields = (
        "reservation_id",
        "reservation_state",
        "reward_points",
        "resource",
        "location",
        "start_time",
        "end_time",
        "queue_percentage",
        "train_percentage",
    )
    # reservation_state = serializers.CharField(max_length=200)
    # resource = serializers.CharField(max_length=200)
    # location = serializers.CharField(max_length=200)
    # start_time = serializers.CharField(max_length=200)
    # end_time = serializers.CharField(max_length=200)
    # reward_points = serializers.IntegerField()