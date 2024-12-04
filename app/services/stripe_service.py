import requests
import base64
from app.utils.env_variables import STRIPE_SECRET_KEY

def create_payment_link(price_id, quantity):
    url = "https://api.stripe.com/v1/payment_links"
    auth_header = base64.b64encode(f"{STRIPE_SECRET_KEY}:".encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_header}",
    }
    data = {
        "line_items[0][price]": price_id,
        "line_items[0][quantity]": quantity,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

