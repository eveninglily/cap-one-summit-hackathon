import time
import random
import classify
import requests
import json
import math
from constants import *
from secret import *

allowed_categories = ["furniture_store", "electronics_store", "bakery", "home_goods_store", "pharmacy"]

def round_to(num, dec_places):
    return round(num * 10 ** dec_places) / (10 ** dec_places)


def generate_purchase():
    min_price = 1.0
    max_price = 200.0

    # 3-week time span
    end_time = int(time.time())
    start_time = end_time - 4 * 7 * 24 * 60 * 60

    purchase_time = time.localtime(random.randint(start_time, end_time))
    time_str = "{:02d}-{:02d}-{:02d}".format(purchase_time.tm_year, purchase_time.tm_mon, purchase_time.tm_mday)
    amount = round_to(random.random() * (max_price - min_price) + min_price, 2)

    return (time_str, amount)


def generate_purchases():
    purchases = {}
    total = 0
    for category in GENERAL_CATEGORIES.keys():
        num_purchases = random.randint(0, 30)
        purchases[category] = [generate_purchase() for _ in range(num_purchases)]
        total += num_purchases
    purchases["other"] = [generate_purchase() for _ in range(100 - total)]
    return purchases

def get_merchants_multi(categories):

    return merchants

# Gets a list of nessie merchants based on category, then filters by zip code
def get_local_merchants(category, zip):
    ret = []
    merchants = get_merchants(category)
    for merchant in merchants:
        if merchant['address']['zip'] == zip:
            ret.append(merchant)
    return ret

def get_local_merchants(categories, zip):
    req = requests.get('http://api.reimaginebanking.com/merchants',
                        params={'key': NESSIE_KEY})
    merchants = []
    print("Searching merchants")
    for merchant in req.json():
        for cat in merchant['category']:
            for c2 in categories:
                if cat == c2:
                    if zip == None:
                        merchants.append(merchant)
                        break
                    else:
                        for z in zip:
                            if merchant['address']['zip'] == z:
                                merchants.append(merchant)
                                break
    return merchants

# Creates a lot of purchases through the nessie API
def generate_nessie_purchases(client):
    purchase_data = generate_purchases()

    merchants = {}
    merchants["other"] = get_local_merchants(allowed_categories, None)
    for category in GENERAL_CATEGORIES.keys():
        print(list(GENERAL_CATEGORIES[category]))
        merchants[category] = get_local_merchants(list(GENERAL_CATEGORIES[category]), None)
    for category in purchase_data:
        for purchase in purchase_data[category]:
            i = math.floor(random.random() * len(merchants[category]))
            id = merchants[category][i]["_id"]
            create_nessie_purchase(client, id, list(purchase)[0], list(purchase)[1], "Purchase")


def create_nessie_purchase(id, merchant, date, amount, desc):
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

if __name__ == "__main__":
    generate_nessie_purchases("5a563d1b5eaa612c093b0b1e")
