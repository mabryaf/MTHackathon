from django.test import TestCase

# Create your tests here.
import uuid # unique IDs for queues

# users = [
#     {
#         "person_id": uuid.uuid1().hex,
#         "name": "Jerry Overton"
#     },
#     {
#         "person_id": uuid.uuid1().hex,
#         "name": "Abhinav Chaudhary"
#     },
#     {
#         "person_id": uuid.uuid1().hex,
#         "name": "Mabry Fonseca"
#     },
#     {
#         "person_id": uuid.uuid1().hex,
#         "name": "Abhishek Kumar"
#     },
#     {
#         "person_id": uuid.uuid1().hex,
#         "name": "Hitesh Kumar"
#     },
#     {
#         "person_id": uuid.uuid1().hex,
#         "name": "Diwakar Peddinti"
#     },
# ]

users = [
    {
        "person_id": "e973d45cc5c911eaa2ba0242ac100002",
        "name": "Jerry Overton",
        "reward_points": 100
    },
    {
        "person_id": "e973d556c5c911eaa2ba0242ac100002",
        "name": "Abhinav Chaudhary",
        "reward_points": 100
    },
    {
        "person_id": "e973d61ec5c911eaa2ba0242ac100002",
        "name": "Mabry Fonseca",
        "reward_points": 100
    },
    {
        "person_id": "e973d6d2c5c911eaa2ba0242ac100002",
        "name": "Abhishek Kumar",
        "reward_points": 100
    },
    {
        "person_id": "e973d77cc5c911eaa2ba0242ac100002",
        "name": "Hitesh Kumar",
        "reward_points": 100
    },
    {
        "person_id": "e973d830c5c911eaa2ba0242ac100002",
        "name": "Diwakar Peddinti",
        "reward_points": 100
    },
]

class Customer(object):
    def __init__(self, **kwargs):
        for field in ('person_id', 'name', 'reward_points'):
            setattr(self, field, kwargs.get(field, None))

customers = {
    1: Customer(person_id="e973d45cc5c911eaa2ba0242ac100002", name="Jerry Overton", reward_points = 100),
    2: Customer(person_id="e973d556c5c911eaa2ba0242ac100002", name="Abhinav Chaudhary", reward_points = 100),
    3: Customer(person_id="e973d61ec5c911eaa2ba0242ac100002", name="Mabry Fonseca", reward_points = 100),
    4: Customer(person_id="e973d6d2c5c911eaa2ba0242ac100002", name="Abhishek Kumar", reward_points = 100),
    5: Customer(person_id="e973d77cc5c911eaa2ba0242ac100002", name="Hitesh Kumar", reward_points = 100),
    6: Customer(person_id="e973d830c5c911eaa2ba0242ac100002", name="Diwakar Peddinti", reward_points = 100),
}

