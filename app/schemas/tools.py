from app.services.stripe_service import retrieve_balance, create_price, create_payment_link, update_payment_link, retrieve_payment_link_line_items, retrieve_payment_link, list_payment_links

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_balance",
            "description": "Retrieve the balance of a Stripe account.",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_price",
            "description": "Create a price for a product using Stripe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "currency": {"type": "string", "description": "Currency code (e.g., 'usd')."},
                    "unit_amount": {"type": "integer", "description": "Amount in cents."},
                    "interval": {"type": "string", "description": "Billing interval (e.g., 'month')."},
                    "product_name": {"type": "string", "description": "Name of the product."},
                },
                "required": ["currency", "unit_amount", "interval", "product_name"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_payment_link",
            "description": "Generate a payment link using Stripe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "price_id": {"type": "string", "description": "Stripe price ID for the product."},
                    "quantity": {"type": "integer", "description": "Quantity of items."},
                },
                "required": ["price_id", "quantity"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_payment_link",
            "description": "Update a payment link with metadata using Stripe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "payment_link_id": {"type": "string", "description": "Stripe payment link ID."},
                    "metadata": {"type": "object", "description": "Metadata to update."},
                },
                "required": ["payment_link_id", "metadata"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "retrieve_payment_link_line_items",
            "description": "Retrieve line items of a payment link using Stripe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "payment_link_id": {"type": "string", "description": "Stripe payment link ID."},
                },
                "required": ["payment_link_id"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "retrieve_payment_link",
            "description": "Retrieve a payment link using Stripe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "payment_link_id": {"type": "string", "description": "Stripe payment link ID."},
                },
                "required": ["payment_link_id"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_payment_links",
            "description": "List all payment links using Stripe.",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
    }
    # add more tools here
]

FUNCTION_MAP = {
    "retrieve_balance": retrieve_balance,
    "create_price": create_price,
    "create_payment_link": create_payment_link,
    "update_payment_link": update_payment_link,
    "retrieve_payment_link_line_items": retrieve_payment_link_line_items,
    "retrieve_payment_link": retrieve_payment_link,
    "list_payment_links": list_payment_links
#  add more functions here
}
