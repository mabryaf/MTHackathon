from . import models
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    # allergic_food = serializers.ListField(allow_empty=True, min_length=None, max_length=None)
    # meal_type = serializers.ListField(allow_empty=True, min_length=None, max_length=None)
    class Meta:
        model = models.Customer
        fields = ['first_name', 'last_name']