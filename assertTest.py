import pytest
import requests

from pytest_check import check
from pytest import assume


URL_BASE = "https://httpbin.org/post"

def test_assert():
    payload = {"username": "admin", "password": "123456"}
    r = requests.post(URL_BASE, json=payload)
    print("状态码", r.status_code)
    print("返回", r.json())

    # #status_code断言
    # assert r.status_code == 200
    #
    # #value
    # assert r.json()["json"]["username"] == "admin"
    # assert r.json()["json"]["password"] == "123456"
    #
    # #exits
    # assert "username" in r.json()["json"]
    #
    # #length
    # assert len(r.json()["json"]) == 3
    #
    # #type
    # assert isinstance(r.json()["json"], int)
    #
    # #time
    # assert r.elapsed.total_seconds() < 1
    #
    # #included
    # assert "admin" in r.json()["json"]["username"]
    #
    # #not included
    # assert r.status_code != 404

    # status_code断言
    # pytest.assume(r.status_code == 200)
    #
    # # value
    # pytest.assume(r.json()["json"]["username"] == "admin")
    # pytest.assume(r.json()["json"]["password"] == "123456")
    #
    # # exits
    # pytest.assume("username" in r.json()["json"])
    #
    # # length
    # pytest.assume(len(r.json()["json"]) == 2)
    #
    # # type
    # pytest.assume(isinstance(r.json()["json"], dict))
    #
    # # time
    # pytest.assume(r.elapsed.total_seconds() < 5)
    #
    # # included
    # pytest.assume("admin" in r.json()["json"]["username"])
    #
    # # not included
    # pytest.assume(r.status_code != 404)

    #status_code断言
    with assume: assert r.status_code == 200

    #value
    with assume: assert r.json()["json"]["username"] == "admin"
    with assume: assert r.json()["json"]["password"] == "123456"

    #exits
    with assume: assert "username" in r.json()["json"]

    #length
    with assume: assert len(r.json()["json"]) == 3

    #type
    with assume: assert isinstance(r.json()["json"], int)

    #time
    with assume: assert r.elapsed.total_seconds() < 5

    #included
    with assume: assert "admin" in r.json()["json"]["username"]

    #not included
    with assume: assert r.status_code != 404

    print("用例执行完毕")