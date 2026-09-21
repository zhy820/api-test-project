import pytest
import requests

BASE_URL = "https://httpbin.org"

@pytest.fixture
def login_token():
    url = f"{BASE_URL}/post"
    payload = {"username": "admin", "password": "123456"}
    r = requests.post(url, json=payload)
    assert r.status_code == 200
    token = r.json()["json"]["password"]
    # return token
    yield token

    print("Logout or cleanup actions can be performed here if needed.")