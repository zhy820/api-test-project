import requests

BASE_URL = "https://httpbin.org"

def test_protected_api(login_token):
    headers = {"Authorization": f"Bearer {login_token}"}
    r = requests.get(f"{BASE_URL}/get", headers=headers)
    assert r.status_code == 200
    assert r.json()["headers"]["Authorization"] == f"Bearer {login_token}"