from django.test import TestCase
import requests, jsonpath, json
from rest_framework import response

url = 'http://localhost:8000/api/leads/3/'

# response = requests.get(url)
# print(response.json())
data = {
    "name": "Ololade Kauthar",
    "email": "ola23@gmail.com",
    "message": "I love you more than you think"
}

headers = {
    "Content-Type": "application/json"
}

# response = requests.put(url, data)
print(response.json())
# assert response.status_code == 200