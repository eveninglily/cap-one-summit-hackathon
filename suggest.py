from secret import *
import requests
import random
import math
import json

prefs = {
    "bar": ["gym", "bowling_alley"],
    "liquor_store": ["grocery_or_supermarket", "cafe"],
    "meal_takeaway": ["grocery_or_supermarket"],
    "meal_delivery": ["grocery_or_supermarket"],
    "shopping_mall": ["book_store", "library", "zoo", "spa", "museum"],
    "department_store": ["book_store", "library", "zoo", "spa", "museum"],
    "clothing_store": ["book_store", "library", "zoo", "spa", "museum"],
    "casino": ["movie_theater", "book_store", "library", "zoo", "spa", "museum"]
}

def suggest_alternative(lat, lng, category, prefs):
    i = math.floor(len(prefs[category]) * random.random())
    type = prefs[category][i]
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

print(suggest_alternative(38.878337, -77.100703, "casino", prefs))