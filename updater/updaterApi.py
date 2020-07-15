import requests
from smartqueue.models import Resource
from smartqueue.smartqueue import sq
import json

def _get_json():
    r = requests.get("https://smartqueueapi.azurewebsites.net/resource/")
    r = json.loads(r.text)

    try:
        r.raise_for_status()
        return r
    except:
        return None

      
def update_smartqueue():
    json = _get_json()
    if json is not None:
        try:
            # new_forecast = Forecast()
            sq.update(json)
            
            # open weather map gives temps in Kelvin. We want celsius.              
            # temp_in_celsius = json['main']['temp'] - 273.15
            # new_forecast.temperatue = temp_in_celsius
            # new_forecast.description = json['weather'][0]['description']
            # new_forecast.city = json['name']
            # new_forecast.save()
            # print("saving...\n" + new_forecast)
        except:
            pass