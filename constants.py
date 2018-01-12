from collections import OrderedDict

CUSTOMER_ID = "5a563d3b5eaa612c093b0ba2"
API_ROOT = "http://api.reimaginebanking.com"
GENERAL_CATEGORIES = OrderedDict([
    ("drinking_and_gambling", {"bar", "casino", "liquor_store"}),
    ("shopping", {"clothing_store", "department_store", "shoe_store", "shopping_mall"}),
    ("food", {"meal_takeaway", "restaurant"})
    ])

PREFS = {
        "bar": ["gym", "bowling_alley"],
        "liquor_store": ["grocery_or_supermarket", "cafe"],
        "meal_takeaway": ["grocery_or_supermarket"],
        "meal_delivery": ["grocery_or_supermarket"],
        "shopping_mall": ["book_store", "library", "zoo", "spa", "museum"],
        "department_store": ["book_store", "library", "zoo", "spa", "museum"],
        "clothing_store": ["book_store", "library", "zoo", "spa", "museum"],
        "casino": ["movie_theater", "book_store", "library", "zoo", "spa", "museum"]
        }

