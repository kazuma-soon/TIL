# translator.pyのGoogleTranslatorを呼び出してテスト

from translator import GoogleTranslator
import pytest

# 前処理の設定
@pytest.fixture(scope="module")
def trans():
    t = GoogleTranslator()
    print("create Translator")
    return t

# def test_japanese_to_english(trans, mocker):
#     mocker.patch('translator.GoogleTranslator.convert', return_value='My name is Sato.')
#     text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
#     assert text_translated == "My name is Sato."

def test_english_to_japanese(trans, mocker):
    def param_select(param):
        if param == '英語':
            return 'en'
        else:
            return 'fr'
    mocker.patch('translator.GoogleTranslator.get_language_id', side_effect = param_select)
    text_translated = trans.convert("My name is Sato.", "英語", "フランス語")
    print(text_translated)
