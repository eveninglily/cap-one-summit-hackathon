import requests
import secret

CUSTOMER_ID = "5a563d3b5eaa612c093b0ba2"

get_params = {"id": CUSTOMER_ID, "key": secret.NESSIE_KEY}
