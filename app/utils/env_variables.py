import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the Stripe secret key
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

# Check if the Stripe secret key is set
if not STRIPE_SECRET_KEY:
    raise ValueError("STRIPE_SECRET_KEY is not set in environment variables")

# Retrieve the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if the OpenAI API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in environment variables")
