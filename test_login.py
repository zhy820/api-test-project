import requests

BASE_URL = "https://httpbin.org"

def test_login():
    url = f"{BASE_URL}/post"
    payload = {"username": "admin", "password": "123456"}
    r = requests.post(url, json=payload)
    print("状态码:", r.status_code)
    print("返回:", r.json())
    assert r.status_code == 200
    assert r.json()["json"]["username"] == "admin"

def test_with_header():
    url = f"{BASE_URL}/get"
    headers = {"User-Agent": "pytest-demo", "Authorization": "Bearer fake-token-123"}
    r = requests.get(url, headers=headers)
    assert r.status_code == 200
    assert r.json()["headers"]["Authorization"] == "Bearer fake-token-123"

def test_protected_api():
    token = "fake-token-123"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"{BASE_URL}/get", headers=headers)
    assert r.status_code == 200
    assert r.json()["headers"]["Authorization"] == f"Bearer {token}"