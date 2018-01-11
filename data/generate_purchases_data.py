import time
import random
import classify
from constants import *

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

if __name__ == "__main__":
    p = generate_purchases()
    classify.process(p)
