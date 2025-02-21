import requests

TELEGRAM_TOKEN = "7706675741:AAGoJGGUnapN71BIHP1qalxVGqW4PSnoku8"
CHAT_ID = "1086859780"

def send_test_message():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": "this is a test message."
    }
    
    response = requests.get(url, params=params)
    print(response.json())  # This will show if the request was successful

send_test_message()
