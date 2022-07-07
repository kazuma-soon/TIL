# メソッドのテスト
class TestExample():
    def example1(self):
        return True

    def test_example2(self):
        assert True

def test_hello_world():
    print('hello world!')
    
def test_a():
    a = TestExample()
    assert a.example1() == True