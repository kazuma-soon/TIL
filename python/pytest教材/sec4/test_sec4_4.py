# モジュールに対する前処理＆後処理
import pytest

@pytest.fixture(scope="module") # scopeはフィクスチャ関数が実行される粒度を指定
def setup_module(request):
    print("setup_module")
    def teardown_module():
        print("teardown_module")
    request.addfinalizer(teardown_module)

@pytest.fixture(scope="function") # scopeはフィクスチャ関数が実行される粒度を指定
def setup_function(request):
    print("setup_function")
    def teardown_function():
        print("teardown_function")
    request.addfinalizer(teardown_function)

def test_hello_world(setup_module, setup_function):
    print("hello world!")

def test_pytest(setup_module):
    print("pytest")

class TestExample():
    def test_hello_world(self, setup_module):
        print("hello world!")

    def test_pytest(self, setup_module):
        print("pytest")