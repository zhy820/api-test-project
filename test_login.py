import requests
from numpy.f2py.crackfortran import usepattern

BASE_URL = "https://httpbin.org"
#BASE_URL = "https://baidu.com"


'''Login API 测试'''
# def test_login():
#     url = f"{BASE_URL}/post"
#     payload = {"username": "admin", "password": "123456"}
#     r = requests.post(url, json=payload)
#     print("状态码", r.status_code)
#     print("返回", r.json())
#
#     assert r.status_code == 200
#     assert r.json()["json"]["username"] == "admin"

# '''GET API 测试'''
# def test_with_header():
#     url = f"{BASE_URL}/get"
#     hearders ={"User-Agent": "pytest-demo", "Authorization": "Bearer fake"}
#
#     r = requests.request(method = "GET", url = url, headers = hearders)
#
#     print("GET 状态码", r.status_code)
#     print("Json打印", r.json())
#
#     assert r.status_code == 200
#     assert r.json()["headers"]["Authorization"] == "Bearer fake"
#
# '''Token API 测试'''
# def test_with_protected_api():
#     token = "fake-token-123"
#     headers = {"Authorization": f"Bearer"}
#
#     #r.requests(method = "GET", url = f"{BASE_URL}/get", headers = headers)
#     r =  requests.get(url = f"{BASE_URL}/get", headers = headers)
#     assert r.status_code == 200
#     assert r.json()["headers"]["Authorization"] == f"Bearer {token}"


'''Real API 测试'''
def test_real_api():
    #Login
    url = f"{BASE_URL}/post"
    payload = {"username": "admin", "password": "123456"}
    r = requests.post(url, json=payload)
    print("状态码", r.status_code)
    print("返回", r.json())

    assert r.status_code == 200
    assert r.json()["json"]["username"] == "admin"

    #Get Token
    token = r.json()["json"]["password"]
    hearders = {"User-Agent": "pytest-demo",
                "Authorization": f"Bearer {token}"}
    r = requests.get(url = f"{BASE_URL}/get", headers = hearders)

    print("GET 状态码", r.status_code)
    print("Json打印", r.json())