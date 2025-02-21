import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_test_message():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": "this is a test message."
    }
    
    response = requests.get(url, params=params)
    print(response.json())  # This will show if the request was successful

send_test_message()
