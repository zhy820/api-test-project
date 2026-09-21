import json
import pytest
import requests
from jsconschema import validate, ValidationError

BASE_URL = "https://httpbin.org"

def load_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_post_schema():
    url = f"{BASE_URL}/post"
    r = requests.post(url, json={"username": "admin", "password": "123456"})
    print("状态码", r.status_code)
    assert r.status_code == 200

    schema = load_schema("data/user_schema.json")
    validate(instance=r.json()["json"], schema=schema)
