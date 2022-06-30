from janome.tokenfilter import LowerCaseFilter
from janome.analyzer import Analyzer
from jaconv import kata2hira
from .janomeCustomDict.tokenizer import tokenizer


tokenFilters = [LowerCaseFilter()]
analyzer = Analyzer([], tokenizer, tokenFilters)

# 全角英数字を半角に変化するための対応辞書
translateDict = {
    **{chr(0xFF10 + i): chr(0x30 + i) for i in range(10)},  # 全角数字: 半角数字
    **{chr(0xFF21 + i): chr(0x41 + i) for i in range(26)},  # 全角英大文字: 半角英大文字
    **{chr(0xFF41 + i): chr(0x61 + i) for i in range(26)},  # 全角英小文字: 半角英小文字
}


def hiraganize(query):
    reading = ""
    for token in tokenizer.tokenize(query):
        if token.reading != "*":
            reading += token.reading
        else:
            reading += token.base_form
    return kata2hira(reading)


def replaceToHalfwidth(text) -> str:
    # http://eneprog.blogspot.com/2018/09/pythonunicodedata.html
    # https://qiita.com/YuukiMiyoshi/items/6ce77bf402a29a99f1bf
    # 直接returnすると型推論が上手くいかないので一旦代入してstrであることを明示する
    s: str = text.translate(str.maketrans(translateDict))
    return s
