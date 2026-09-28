import allure
import pytest
from utils.api_client import ApiClient
from config.settings import BASE_URL, USERNAME, PASSWORD

BASE_URL = f"{BASE_URL}"

@pytest.fixture(scope="session")
def api():
    return ApiClient(BASE_URL)

@allure.feature("Login Feature")
@allure.story("Valid Login Test")
@allure.title("Using Valid user and pwd to login")
def test_login(api):
    with allure.step("Login Test"):
        r = api.post("/post", json={"username": "admin", "password": "123456"})

    with allure.step("Verify the satus"):
        assert r.status_code == 200

    with allure.step("Verify the username"):
        assert r.json()["json"]["username"] == "admin"


@allure.feature("Get Feature")
@allure.story("Get information Test")
@allure.title("Get Get test information")
def test_get(api):
    with allure.step("GET GET Test"):
        r = api.get("/get")

    with allure.step("Verify the status"):
        assert r.status_code == 200

    allure.attach(r.text, name= "Response Body", attachment_type=allure.attachment_type.TEXT)

