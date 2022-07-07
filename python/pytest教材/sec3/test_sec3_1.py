def setup_function(function):
    print('setup_function')
    print(function)

def teardown_function(function):
    print('teardown_function')

def test_hello_world():
    print("hello world!")

def test_pytest():
    print("pytest")
