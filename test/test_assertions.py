import pytest

from test.test_schema import BASE_URL
from utils.api_client import ApiClient
from utils.assertions import assert_status, assert_json_value
from utils.data_factory import random_password, random_username

BASE_URL = "https://httpbin.org"

@pytest.fixture(scope="session")
def api():
    return ApiClient(BASE_URL)

def test_login(api):
    username = random_username()
    password = random_password()
    r = api.post("/post", json={"username": username, "password": password})

    assert_status(r, 200)
    assert_json_value(r, "json.username", username)

