import os
from janome.tokenizer import Tokenizer

customDictPath = os.path.join(os.path.dirname(__file__), "dict.csv")
tokenizer = Tokenizer(customDictPath, udic_enc="utf-8")
