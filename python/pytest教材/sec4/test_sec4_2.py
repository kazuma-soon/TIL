import pytest

@pytest.fixture(scope='class')
def start(request):
    print('fixture-start')
    
    def end():
        print('fixture-end')
    request.addfinalizer(end)


class TestExample():
    def test_example1(self, start):
        print("hello world!")

    def test_example2(self, start):
        print("pytest!")
    
