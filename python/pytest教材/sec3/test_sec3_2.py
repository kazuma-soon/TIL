# 前処理＆後処理のメソッドの作成
class TestExample():
    # 前処理の実行
    def setup_method(self):
        print("setup_method")

    # 後処理の実行
    def teardown_method(self):
        print("teardown_method")

    def test_example1(self):
        print("hello world!")

    def test_example2(self):
        print("pytest!")
