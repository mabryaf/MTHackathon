from django.db import models

class Customer(models.Model):

    # id = models.IntegerField()
    first_name = models.CharField(max_length = 255, default = '', blank = True)
    last_name = models.CharField(max_length = 255, default = '', blank = True)

    class Meta:
        db_table = 'customer'
        managed = False

# class Trains(models.Model):
#     id = models.IntegerField()
#     trip_update = models.CharField(max_length=200)
# Create your models here.


# id: "000001"
# trip_update {
#   trip {
#     trip_id: "057150_1..N03R"
#     start_date: "20200630"
#     route_id: "1"
#   }
#   stop_time_update {
#     arrival {
#       time: 1593527567
#     }
#     stop_id: "101N"
#   }
# }

# {
#     "model": "opinion_ate.restaurant",
#     "pk": 1,
#     "fields": {
#       "name": "Sushi Place",
#       "address": "123 Main Street"
#     }
