import requests
import json
from smartqueue.smartqueue import sq


#Retrieve the smartqueue schedule and convert to json
def _get_json():
    r = requests.get("https://smartqueueapi.azurewebsites.net/resource/")

    try:
        r.raise_for_status()
        return json.loads(r.text)
    except:
        return None

      
def update_smartqueue():
    json = _get_json()
    if json is not None:
        try:
            sq.update(json)
        except:
            pass