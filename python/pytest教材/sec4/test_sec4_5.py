import pytest

# 前処理＆後処理の定義
@pytest.fixture(autouse=True) # デフォルトはFalse
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

class TestExample():
    def test_hello(self):
        print("hello")

    def test_goodmorning(self):
        print("goodmorning")

    def test_goodafternoon(self):
        print("goodafternoon")
