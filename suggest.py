from secret import *
import requests
import random
import math
import json

from constants import PREFS


def suggest_alternative(lat, lng, category, PREFS):
    i = math.floor(len(PREFS[category]) * random.random())
    type = PREFS[category][i]
    #print(type)
    req = requests.get(
        'https://maps.googleapis.com/maps/api/place/nearbysearch/json?',
        params={
            'key': PLACES_KEY,
            'location': "{},{}".format(lat, lng),
            'radius': 1609 * 2,
            'type': type
        }
    )

    # Return top 5 suggestions
    #print(json.dumps(req.json()["results"][0], indent=4))
    cleaned = []
    for data in req.json()["results"][:5]:
        d = {}
        d['name'] = data['name']
        d['lat'] = data['geometry']['location']["lat"]
        d['lng'] = data['geometry']['location']["lng"]
        cleaned.append(d)
    return cleaned

if __name__ == "__main__":
    print(suggest_alternative(38.878337, -77.100703, "casino", PREFS))