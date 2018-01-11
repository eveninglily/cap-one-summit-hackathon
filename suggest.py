from secret import *
import requests
import random
import math
import json

def suggest_alternative(lat, lng, category, prefs):
    i = math.floor(len(prefs[category]) * random.random())
    type = prefs[category][0]
    req = requests.get(
        'https://maps.googleapis.com/maps/api/place/nearbysearch/json?',
        params={
            'key': PLACES_KEY,
            'location': "{},{}".format(lat, lng),
            'radius': 1609 * 2,
            'maxprice': 2,
            'type': 'art_gallery'
        }
    )

    # Return top 5 suggestions
    print(json.dumps(req.json(), indent=4))

suggest_alternative(38.878337, -77.100703, "bar", {"bar":"art_gallery"})