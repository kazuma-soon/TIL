# テストのスキップ
import pytest

def test_hello():
    print("hello")

@pytest.mark.morning
def test_goodmorning():
    print("goodmorning")

@pytest.mark.afternoon
def test_goodafternoon():
    print("goodafternoon")
