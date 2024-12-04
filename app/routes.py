import json
import logging

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.services import opensearch_service, openai_service
from app.schemas.tools import FUNCTION_MAP as available_tools

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

    messages = [{"role": "system", "content": "You are a helpful Stripe Chatbot assistant."}]
    for entry in context:
        role = "assistant" if entry["sender"] == "system" else "user"
        messages.append({"role": role, "content": entry["message"]})
    messages.append({"role": "user", "content": user_message})

    response = openai_service.generate_response(messages)
    choice = response.choices[0]

    system_response = choice.message.content
    completion_tool_calls = choice.message.tool_calls

    if completion_tool_calls:
        for call in completion_tool_calls or []:
            tool_to_call = available_tools[call.function.name]
            args = json.loads(call.function.arguments)
            result = tool_to_call(**args)
            
            return jsonify({"response": json.dumps(result)})

        if system_response:
            opensearch_service.save_message_to_opensearch(system_response, "system")
        else:
            return jsonify({"error": "No response from OpenAI"}), 500    
    return jsonify({"response": system_response})
