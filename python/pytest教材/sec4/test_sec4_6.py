# テストのスキップ
import pytest

def test_hello():
    print("hello")

@pytest.mark.skip(reason="write reason")
def test_goodmorning():
    print("goodmorning")

def test_goodafternonn():
    print("goodafternoon")
