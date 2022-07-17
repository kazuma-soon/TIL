# モジュールに対する前処理＆後処理
import pytest

@pytest.fixture(scope='module')
def setup_module(request):
    print('start')
    def teardown_module():
        print('end')
    request.addfinalizer(teardown_module)

def test_hello_world(setup_module):
    print("hello world!")

def test_pytest(setup_module):
    print("pytest")

class TestExample():
    def test_hello_world(self, setup_module):
        print("hello world!")

    def test_pytest(self, setup_module):
        print("pytest")