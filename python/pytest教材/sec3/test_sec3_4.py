def setup_class(module):
    print('start')

    
def teardown_module(module):
    print('end')

def test_hello_world():
    print("hello world!")

def test_pytest():
    print("pytest")

class TestExample():
    def test_hello_world(self):
        print("hello world!")

    def test_pytest(self):
        print("pytest")