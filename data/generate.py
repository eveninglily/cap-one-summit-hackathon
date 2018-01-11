from secret import *
import requests
import json

def filter_merchants(category):
    req = requests.get('http://api.reimaginebanking.com/merchants',
                        params={'key': NESSIE_KEY})
    for merchant in req.json():
        for cat in merchant['category']:
            if cat == category:
                print(merchant['name'])
                print(merchant['_id'])

def create_purchase(id, merchant, date, amount, desc):
    req = requests.post(
        'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(id, NESSIE_KEY),
        json={
            "merchant_id": merchant,
            "medium": 'balance',
            "purchase_date": date,
            "amount": amount,
            "status": 'completed',
            "description": desc
        }
    )
    print(req.content)