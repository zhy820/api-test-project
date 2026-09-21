import os
import pytest
import requests
from utils.data_loader import load_yaml

BASE_URL = "https://httpbin.org"
DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data", "login_cases.yaml"
)

cases = load_yaml(DATA_FILE)
print("DATA_FILE", DATA_FILE)

@pytest.mark.parametrize("case", cases)
def test_login_data_driven(case):
    r = requests.post(
        f"{BASE_URL}/post",
        json={"username": case["username"], "password": case["password"]}
    )
    assert r.status_code == case["expected_status"]
    assert r.json()["json"]["username"] == case["username"]