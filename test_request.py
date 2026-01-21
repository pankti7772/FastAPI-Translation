import requests
import json

url = "http://localhost:8000/translate"
payload = {"text": "Hello, how are you?"}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
    print("Ensure the server is running on localhost:8000")
