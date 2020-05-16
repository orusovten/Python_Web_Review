import pytest
from encode_engine import do_operation, find_errors_in_text


def test_caesar_encode():
    words = ["abc", "jifdngreop!", "4$google_tengisahaha"]
    keys = [3, 20, 100]
    right_answers = ["def", "DCzxHALyIJ?", "9)lttlqj~yjslnxfmfmf"]
    for word, key, right_answer in zip(words, keys, right_answers):
        assert do_operation(word, "encode", "caesar", key) == right_answer


def test_vigenere_encode():
    words = ["Very good story!", "Do you hear me?", "#78kjnchrnaE"]
    keys = ["Hello", "No", "Abracadbra"]
    right_answers = ["{iCJnNszonZxzCM1", """;CMM"IMvRo%nZsq""", "{8oklnfiInAF"]
    for word, key, right_answer in zip(words, keys, right_answers):
        assert do_operation(word, "encode", "vigenere", key) == right_answer


def test_caesar_decode():
    words = ["abc", "ERTdsffdvhuih5^&?827390", "dnfnooame 33"]
    keys = [3, 46, 121]
    right_answers = ["89 ", "`8 !:##!=%<&%RFlAUOTPVM", "?}[}~~<|@;**"]
    for word, key, right_answer in zip(words, keys, right_answers):
        assert do_operation(word, "decode", "caesar", key) == right_answer


def test_vigenere_decode():
    words = ["(fClq", """_sw*yqkFdTe:(HCs*nubvx2i"[Vdt~fLn""", """["TxBpvSsyJ"WxAd"""]
    keys = ["Abracadbra", "Het*arcneh1#%", "INFjndhusk"]
    right_answers = ["Hello", "Today is Monday and it`s so awful", "Ooooomoyaoborona"]
    for word, key, right_answer in zip(words, keys, right_answers):
        assert do_operation(word, "decode", "vigenere", key) == right_answer


def test_caesar_encode_and_decode_together():
    words = ["Write me if u can", "123 is a Password!", "Moijvmfzk04&62^^21"]
    keys = [34, 45, 123]
    for word, key in zip(words, keys):
        encode_result = do_operation(word, "encode", "caesar", key)
        assert word == do_operation(encode_result, "decode", "caesar", key)


def test_vigenere_encode_and_decode_together():
    words = ["Write me if u can", "123 is a Password!", "Moijvmfzk04&62^^21"]
    keys = ["abc", "ahdejncuhdn", "%4$sdrQ^:"]
    for word, key in zip(words, keys):
        encode_result = do_operation(word, "encode", "vigenere", key)
        assert word == do_operation(encode_result, "decode", "vigenere", key)


def test_caesar_break():
    with open("text_for_testing_caesar_break.txt", "r") as file:
        text = file.read()
        keys = [1, 100, 20]
        for key in keys:
            ciphered_text = do_operation(text, "encode", "caesar", key)
            assert text == do_operation(ciphered_text, "caesar_break")


def test_find_errors_in_text():
    empty_text = ""
    assert "Please, enter the text" == find_errors_in_text(empty_text)
    texts_with_wrong_symbols = ["Try to calculate this: ε + 1 = ρ(Ω)", "νγρθσσ"]
    for text in texts_with_wrong_symbols:
        assert "{!r} is not consist of Alphabet symbols.".format(text) == find_errors_in_text(text)
