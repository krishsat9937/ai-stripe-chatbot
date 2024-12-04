create_payment_link_function_schema = {
    "name": "create_payment_link",
    "description": "Generate a payment link using Stripe.",
    "parameters": {
        "type": "object",
        "properties": {
            "price_id": {
                "type": "string",
                "description": "Stripe price ID for the product.",
            },
            "quantity": {"type": "integer", "description": "Quantity of items."},
        },
        "required": ["price_id", "quantity"],
    },
}
