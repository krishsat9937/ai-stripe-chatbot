
import openai
import logging

from app.utils.env_variables import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Set up logging
logging.basicConfig(level=logging.INFO)


def generate_response(messages, function_schema):
    """
    Generate a response using OpenAI's chat model.
    
    Args:
        messages (list): A list of message dictionaries with roles ('system', 'user', 'assistant') and content.
        function_schema (dict): Schema for defining function calls in OpenAI chat completion.

    Returns:
        dict: A dictionary containing the AI's response, including content and optional function call details.
    """
    try:

        logging.info(f"Generating response for messages: {messages} and function schema: {function_schema}")
        # Generate response using OpenAI's Chat API
        response = openai.chat.completions.create(
            model="gpt-4-0613",  # Use the model of your choice
            messages=messages,
            functions=[function_schema],
            function_call="auto"  # Automatically decide whether to use a function call
        )

        logging.info(f"OpenAI response: {response}")
        
        return response
    except Exception as e:
        # Log or handle errors gracefully
        print(f"OpenAI API Error: {str(e)}")
        return {"content": None, "function_call": None}
