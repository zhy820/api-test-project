import pytest
from utils.api_client import ApiClient

BASE_URL = "https://httpbin.org"

# @pytest.fixture(scope="session")
@pytest.fixture(scope="function")
def api():
    return ApiClient(BASE_URL)

def test_get(api):
    r = api.get("/get")
    assert r.status_code == 200

def test_post(api):
    r = api.post("/post", json={"username": "admin", "password": "123456"})
    assert r.status_code == 200
    assert r.json()["json"]["username"] == "admin"

def test_put(api):
    r = api.put("/put", json={"username": "admin", "password": "123456"})
    assert r.status_code == 200

def test_delete(api):
    r = api.delete("/delete")
    assert r.status_code == 200
