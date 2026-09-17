import sys

import pytest

@pytest.mark.skipif(sys.version_info < (3, 8), reason="需要 Python 3.8+")

def test_python_version():
    assert sys.version_info >= (3, 8)
    print("python版本符合要求")