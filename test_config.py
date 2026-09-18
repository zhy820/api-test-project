import requests
from config.settings import BASE_URL, USERNAME, PASSWORD

def test_login_with_config():
    url = f"{BASE_URL}/post"
    payload = {"username": USERNAME, "password": PASSWORD}
    r = requests.post(url, json=payload)
    print("状态码", r.status_code)
    print("返回", r.json())

    assert r.status_code == 200
    assert r.json()["json"]["username"] == USERNAME