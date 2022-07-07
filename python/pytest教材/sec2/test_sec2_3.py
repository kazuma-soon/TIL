# 様々な関数のテストを例示
from typing import Text


def test_calculate():
    result = 5 * 2
    assert result == 10

def test_len():
    text = "hello world!"
    assert len(text) == 12

def test_contain():
    text = "hello world!"
    assert "rld" in text