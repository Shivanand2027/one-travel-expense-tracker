import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# URL for the Gemini Pro model
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def check_gemini_api():
    if not GEMINI_API_KEY:
        print("❌ Gemini API key not found. Please set GEMINI_API_KEY in your .env file.")
        return

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [{
            "parts": [{
                "text": "Hello! Can you hear me?"
            }]
        }]
    }

    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        print("✅ Gemini API key is valid!")
        result = response.json()
        print("Response:", result['candidates'][0]['content']['parts'][0]['text'])
    elif response.status_code == 403:
        print("❌ Access Denied: Invalid or unauthorized API key.")
    elif response.status_code == 404:
        print("❌ Model not found: Please check the model name.")
    elif response.status_code == 401:
        print("❌ Unauthorized: Invalid API key.")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    check_gemini_api()
