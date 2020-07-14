from django.test import TestCase

# Create your tests here.
import uuid # unique IDs for queues
import json


users = [
    {
        "person_id": uuid.uuid1().hex,
        "name": "Jerry Overton"
    },
    {
        "person_id": uuid.uuid1().hex,
        "name": "Abhinav Chaudhary"
    },
    {
        "person_id": uuid.uuid1().hex,
        "name": "Mabry Fonseca"
    },
    {
        "person_id": uuid.uuid1().hex,
        "name": "Abhishek Kumar"
    },
    {
        "person_id": uuid.uuid1().hex,
        "name": "Hitesh Kumar"
    },
    {
        "person_id": uuid.uuid1().hex,
        "name": "Diwakar Peddinti"
    },
]

class Customer(object):
    def __init__(self, **kwargs):
        for field in ('person_id', 'name'):
            setattr(self, field, kwargs.get(field, None))

customers = {
    1: Customer(person_id=uuid.uuid1().hex, name="Jerry Overton"),
    2: Customer(person_id=uuid.uuid1().hex, name="Abhinav Chaudhary"),
    3: Customer(person_id=uuid.uuid1().hex, name="Mabry Fonseca"),
    4: Customer(person_id=uuid.uuid1().hex, name="Abhishek Kumar"),
    5: Customer(person_id=uuid.uuid1().hex, name="Hitesh Kumar"),
    6: Customer(person_id=uuid.uuid1().hex, name="Diwakar Peddinti"),
}