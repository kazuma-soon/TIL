from translator import GoogleTranslator
import pytest

def test_mock_exception(mocker):
    mock_obj = mocker.patch("translator.GoogleTranslator.get_language_id")
    mock_obj.side_effect = Exception("ConvertException") # 例外を設定

    with pytest.raises(Exception) as e: # 例外オブジェクトをeとして取得
        trans = GoogleTranslator()
        text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
        print(text_translated)

    print(e.value.args[0])
