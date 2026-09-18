import pytest
import requests

BASE_URL = "https://httpbin.org"

# @pytest.mark.parametrize("username, password",[
#     ("admin", "123456"),
#     ("user1", "password1"),
#     ("user2", "password2")
# ])
#
# def test_login(username, password):
#     url = f"{BASE_URL}/post"
#     payload = {"username": username, "password": password}
#     r = requests.post(url, json=payload)
#     print("状态码", r.status_code)
#     print("返回", r.json())
#
#     assert r.status_code == 200
#     assert r.json()["json"]["username"] == username

#pytestmark = pytest.mark.smoke
#pytestmark = pytest.mark.regression

@pytest.mark.smoke
def test_login1():
    url = f"{BASE_URL}/post"
    payload = {"username": "admin", "password": "123456"}
    r = requests.post(url, json=payload)
    print("状态码", r.status_code)
    print("返回", r.json())

    assert r.status_code == 200
    assert r.json()["json"]["username"] == "admin"

@pytest.mark.regression
def test_login2():
    url = f"{BASE_URL}/post"
    payload = {"username": "user", "password": "123456"}
    r = requests.post(url, json=payload)
    print("状态码", r.status_code)
    print("返回", r.json())

    assert r.status_code == 200
    assert r.json()["json"]["username"] == "user"

@pytest.mark.pressure
def test_login3():
    url = f"{BASE_URL}/post"
    payload = {"username": "reader", "password": "123456"}
    r = requests.post(url, json=payload)
    print("状态码", r.status_code)
    print("返回", r.json())

    assert r.status_code == 200
    assert r.json()["json"]["username"] == "reader"



if __name__ == "__main__":
    import pytest
    import sys
    # 强制指定只跑 smoke 标签，并且把当前文件的路径传进去
    sys.exit(pytest.main(["-m", "smoke", "-v", __file__]))