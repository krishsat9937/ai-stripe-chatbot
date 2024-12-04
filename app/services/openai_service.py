
import openai
import json
import logging

from app.utils.env_variables import OPENAI_API_KEY
from app.schemas.tools import TOOLS

openai.api_key = OPENAI_API_KEY

# Set up logging
logging.basicConfig(level=logging.INFO)


def generate_response(messages):    
    try:
        logging.info(f"Generating response for messages: {messages}")
        # Generate response using OpenAI's Chat API
        response = openai.chat.completions.create(
            model="gpt-4-0613",  # Use the model of your choice
            messages=messages,
            tools=TOOLS,
            # function_call="auto"  # Automatically decide whether to use a function call
        )

        logging.info(f"OpenAI response: {response}")
        
        return response
    except Exception as e:
        # Log or handle errors gracefully
        print(f"OpenAI API Error: {str(e)}")
        return {"content": None, "function_call": None}

def handle_function_call(function_call):
    """
    Dynamically handle function calls returned by OpenAI.
    """
    function_name = function_call.name
    arguments = json.loads(function_call.arguments)

    if function_name in TOOLS:
        tool_function = TOOLS[function_name]["function"]
        return tool_function(**arguments)
    else:
        raise ValueError(f"Unknown function: {function_name}")