import pytest
import requests

BASE_URL = "https://httpbin.org"

@pytest.mark.parametrize("username, password",[
    ("admin", "123456"),
    ("user1", "password1"),
    ("user2", "password2")
])

def test_login(username, password):
    url = f"{BASE_URL}/post"
    payload = {"username": username, "password": password}
    r = requests.post(url, json=payload)
    print("状态码", r.status_code)
    print("返回", r.json())

    assert r.status_code == 200
    assert r.json()["json"]["username"] == username