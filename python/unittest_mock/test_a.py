from unittest import TestCase

def test_1():
    a = 1
    b = 1
    assert a == b

def test_2():
    a = 1
    b = 2
    assert a == b

def third_test():
    raise IndexError('test')
    assert a == b

class Tekitou(TestCase):
    def test_3(self):
        a = 1
        b = 3
        self.assertEqual(a, b)

class TestMine:
    def test_4(self):
        a = 1
        b = 4
        assert a == b

class MyTest:
    def test_5(self):
        a = 1
        b = 5
        assert a == b
