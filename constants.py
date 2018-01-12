from collections import OrderedDict

CUSTOMER_ID = "5a563d3b5eaa612c093b0ba2"
API_ROOT = "http://api.reimaginebanking.com"
GENERAL_CATEGORIES = OrderedDict([
    ("drinking_and_gambling", {"bar", "casino", "liquor_store"}),
    ("shopping", {"clothing_store", "department_store", "shoe_store", "shopping_mall"}),
    ("food", {"meal_takeaway", "restaurant"})
    ])

PREFS = {
        "drinking_and_gambling": ["gym", "bowling_alley", "grocery_or_supermarket", "cafe", "movie_theater", "book_store", "library", "zoo", "spa", "museum"],
        "food": ["grocery_or_supermarket", "grocery_or_supermarket"],
        "shopping": ["book_store", "library", "zoo", "spa", "museum", "book_store", "library", "zoo", "spa", "museum", "book_store", "library", "zoo", "spa", "museum"],
        }
