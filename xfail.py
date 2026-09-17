import pytest

@pytest.mark.xfail(reason = "已知bug，暂时失败")

def test_known_bug():
    assert 2 == 3

