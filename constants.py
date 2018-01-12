from collections import OrderedDict

CUSTOMER_ID = "5a563d3b5eaa612c093b0ba2"
API_ROOT = "http://api.reimaginebanking.com"
GENERAL_CATEGORIES = OrderedDict([
    ("drinking_and_gambling", {"bar", "casino", "liquor_store"}),
    ("shopping", {"clothing_store", "department_store", "shoe_store", "shopping_mall"}),
    ("food", {"meal_takeaway", "restaurant"})
    ])
