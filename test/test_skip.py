import sys
import pytest
from pytest import assume


@pytest.mark.skip(reason="Skipping this test for demonstration purposes.")
def test_not_ready():
    with assume: assert False

@pytest.mark.skip(reason = "function not online")
def test_not_online():
    with assume: assert False

@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
def test_skip_if():
    with assume: assert False

#运行时跳过
def test_runtime_skip():
    if sys.platform == "win32":
        pytest.skip("Skipping on Windows platform.")
    with assume: assert True

print("测试完毕！")