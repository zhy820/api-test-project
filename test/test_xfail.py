import sys
import pytest

@pytest.mark.xfail(reason = "已知bug，暂时失败")
def test_known_bug():
    assert 2 == 3

@pytest.mark.xfail(strict=True, reason="必须失败")
def test_must_fail():
    assert 1 == 2

@pytest.mark.xfail(sys.platform== "win32", reason="Windows平台下已知bug")
def test_platform_specific():

    assert 1 == 2

def test_normal():
    assert 1 == 1
