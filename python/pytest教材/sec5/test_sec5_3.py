# 引数によって返り値を複数パターン用意
# translator.pyのGoogleTranslatorを呼び出してテスト
from translator import GoogleTranslator
import pytest

# 前処理の設定
@pytest.fixture(scope="module")
def trans():
    t = GoogleTranslator()
    print("create Translator")
    return t

def test_japanese_to_english(trans, mocker):
    def param_select(param):
        if param == "日本語":
            return "ja"
        else:
            return "fr"
    mocker.patch("translator.GoogleTranslator.get_language_id", side_effect = param_select)
    text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
    print(text_translated)

