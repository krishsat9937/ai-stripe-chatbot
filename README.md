# Flask Chatbot with Stripe Integration

This repository contains a Flask-based chatbot application that integrates with Stripe to generate payment links dynamically. The chatbot is powered by OpenAI's GPT-4 model, allowing it to interpret user input and create payment links for specified products or services.

---

## Features

- **Chatbot Interface:** Accepts user queries and dynamically generates responses.
- **Stripe Integration:** Creates Stripe payment links for specified products and quantities.
- **OpenAI Function Calling:** Uses OpenAI’s function-calling feature to handle structured tasks like balance fetching, price creation, payment link creation etc.
- **CORS Enabled:** Allows frontend applications to communicate with the Flask backend.(Made it simple for MVP, but not good for production)

---

## Prerequisites

1. **Python 3.10+**
2. **Stripe Account**
   - Obtain API keys from the [Stripe Dashboard](https://dashboard.stripe.com/apikeys).
3. **OpenAI Account**
   - Obtain an API key from [OpenAI](https://platform.openai.com/signup/).
4. **Frontend (Optional):** A simple frontend html to interact with the chatbot.

---

## Usage

### 1. Run the Flask Server
```bash
> pip install -r requirements.txt
> python run.py
```

The server will start on `http://127.0.0.1:5000`.

### 2. Test the Chatbot
You can use tools like `Postman` or `curl` to send POST requests:

#### Example Request:
```bash
curl -X POST http://127.0.0.1:5000/chat \
-H "Content-Type: application/json" \
-d '{"message": "Create a payment link for the price id price_1QRdpxDWP6cwTy3QAV6IGeD6 and quantity 1"}'
```

## Frontend Integration

A simple frontend can be added to interact with the chatbot. Use the provided `index.html` file as a starting point. Ensure the Flask server allows CORS requests to enable communication between the frontend and backend.

![Screenshot 2024-12-04 at 3 19 22 PM](https://github.com/user-attachments/assets/518886bb-3426-40c7-b9a4-184f52419240)

---
