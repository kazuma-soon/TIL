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
    mock_obj = mocker.patch("translator.GoogleTranslator.get_language_id")
    mock_obj.side_effect = param_select

    text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
    print(text_translated)

    mock_args = mock_obj.call_args_list
    print(mock_args)
    # assert mock_args[0][0][0] == "日本語"
    # assert mock_args[1][0][0] == "英語"
