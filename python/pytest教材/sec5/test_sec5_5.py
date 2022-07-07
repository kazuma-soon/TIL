# 例外処理の実行
from translator import GoogleTranslator
import pytest

def test_convert():
    with pytest.raises(KeyError):
        trans = GoogleTranslator()
        trans.convert("私の名前は佐藤です。", "日本語", "ポルトガル語")
