import json
import logging

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.services import opensearch_service, openai_service, stripe_service
from app.schemas.function_schemas import create_payment_link_function_schema

# log everything, and send it to stderr
logging.basicConfig(level=logging.INFO)

main = Blueprint('main', __name__)

@main.route("/chat", methods=["POST"])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def chat():
    user_message = request.json.get("message")
    user_id = "user123"

    if not user_message:
        return jsonify({"error": "User message cannot be empty"}), 400

    opensearch_service.save_message_to_opensearch(user_message, user_id)
    context = opensearch_service.get_relevant_context(user_message)

    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for entry in context:
        role = "assistant" if entry["sender"] == "system" else "user"
        messages.append({"role": role, "content": entry["message"]})
    messages.append({"role": "user", "content": user_message})

    response = openai_service.generate_response(messages, create_payment_link_function_schema)
    choice = response.choices[0]

    system_response = choice.message.content

    if choice.message.function_call:
        function_call = choice.message.function_call
        arguments = json.loads(function_call.arguments)
        try:
            payment_link = stripe_service.create_payment_link(
                price_id=arguments["price_id"],
                quantity=arguments["quantity"]
            )
            print("Payment link:", payment_link["url"])
            return jsonify({"response": f"Payment link: {payment_link['url']} (generated using Stripe)"})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    if system_response:
        opensearch_service.save_message_to_opensearch(system_response, "system")
    else:
        return jsonify({"error": "No response from OpenAI"}), 500    
    return jsonify({"response": system_response})
