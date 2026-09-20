from utils.http_client import request

def test_get_get_log():
    r = request("GET","https://httpbin.org/get")

    assert r.status_code == 200

def test_post_with_log():
    r = request("POST","https://httpbin.org/post",json={"username":"admin"})

    assert r.status_code == 200
    assert r.json()["json"] == {"username":"admin"}

    print("JSON TEST:", r.json())