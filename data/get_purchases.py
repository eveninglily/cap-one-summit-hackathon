import requests
from collections import OrderedDict
import sys
sys.path.append('..')
import secret

CUSTOMER_ID = "5a563d3b5eaa612c093b0ba2"
API_ROOT = "http://api.reimaginebanking.com"

GENERAL_CATEGORIES = OrderedDict([
        ("drinking_and_gambling", {"bar", "casino", "liquor_store"}),
        ("shopping", {"clothing_store", "department_store", "shoe_store", "shopping_mall"}),
        ("food", {"meal_takeaway", "restaurant"})
    ])


def get_account_ids(customer_id):
    get_params = {"key": secret.NESSIE_KEY}
    get_request = requests.get("{}/customers/{}/accounts".format(API_ROOT, customer_id), params=get_params)
    return [account["_id"] for account in get_request.json()]

def get_all_purchases(customer_id):
    purchases = []
    for account_id in get_account_ids(customer_id):
        get_params = {"key": secret.NESSIE_KEY}
        get_request = requests.get("{}/accounts/{}/purchases".format(API_ROOT, account_id), params=get_params)
        purchases.extend(
                {"merchant_id": purchase["merchant_id"],
                    "purchase_date": purchase["purchase_date"],
                    "amount": purchase["amount"]}
                for purchase in get_request.json() if purchase["type"] == "merchant")
    return purchases

def get_merchant_categories(merchant_id):
    get_params = {"key": secret.NESSIE_KEY}
    get_request = requests.get("{}/merchants/{}".format(API_ROOT, merchant_id), params=get_params)
    return get_request.json()["category"]

def get_general_category(categories):
    """
    Returns a general category given an array of Google categories.
    """
    for general_category in GENERAL_CATEGORIES:
        if any(category in GENERAL_CATEGORIES[general_category] for category in categories):
            return general_category
    return "other"

def categorize_purchases(purchases):
    categorized_purchases = {category: [] for category in GENERAL_CATEGORIES.keys()}
    categorized_purchases["other"] = []

    for purchase in purchases:
        purchase_general_category = get_general_category(get_merchant_categories(purchase["merchant_id"]))
        purchase_tuple = (purchase["purchase_date"], purchase["amount"])
        categorized_purchases[purchase_general_category].append(purchase_tuple)

    return categorized_purchases

if __name__ == "__main__":
    print(categorize_purchases(get_all_purchases(CUSTOMER_ID)))
