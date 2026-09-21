import requests

def test_det():
    r = requests.get("https://httpbin.org/get")
    print(r.status_code)
    print(r.json())
    assert r.status_code == 200