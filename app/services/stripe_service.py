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
        print(response.json())
        return f"Payment link created: {response.json()['url']}"
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def update_payment_link(payment_link_id, metadata):
    url = f"https://api.stripe.com/v1/payment_links/{payment_link_id}"
    auth_header = base64.b64encode(f"{STRIPE_SECRET_KEY}:".encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_header}",
    }
    data = {
        "metadata[order_id]": metadata,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(response.json())
        return f"Payment link updated: {response.json()}"
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def retrieve_payment_link_line_items(payment_link_id):
    url = f"https://api.stripe.com/v1/payment_links/{payment_link_id}/line_items"
    auth_header = base64.b64encode(f"{STRIPE_SECRET_KEY}:".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


def retrieve_payment_link(payment_link_id):
    url = f"https://api.stripe.com/v1/payment_links/{payment_link_id}"
    auth_header = base64.b64encode(f"{STRIPE_SECRET_KEY}:".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
    

def list_payment_links(limit=100):
    url = "https://api.stripe.com/v1/payment_links"
    auth_header = base64.b64encode(f"{STRIPE_SECRET_KEY}:".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
    }
    params = {
        "limit": limit,
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
    
def retrieve_balance():
    url = "https://api.stripe.com/v1/balance"
    auth_header = base64.b64encode(f"{STRIPE_SECRET_KEY}:".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def create_price(currency, unit_amount, interval, product_name):
    url = "https://api.stripe.com/v1/prices"
    auth_header = base64.b64encode(f"{STRIPE_SECRET_KEY}:".encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_header}",
    }
    data = {
        "currency": currency,
        "unit_amount": unit_amount,
        "recurring[interval]": interval,
        "product_data[name]": product_name,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")