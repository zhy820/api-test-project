import pytest

@pytest.fixture(scope="function")
def func_fixture():
    print("\n[function] 执行")
    return "func"

@pytest.fixture(scope="module")
def module_fixture():
    print("\n[module] 执行")
    return "module"

@pytest.fixture(scope="session")
def session_fixture():
    print("\n[session] 执行")
    return "session"

def test_a(func_fixture, module_fixture, session_fixture):
    print("test_a 执行")

def test_b(func_fixture, module_fixture, session_fixture):
    print("test_b 执行")