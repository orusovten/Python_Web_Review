import pytest
from processing import do_operation


def test_encode_1():
    assert do_operation("abc", "encode", "caesar", 3) == "def"


def test_encode_2():
    assert do_operation("jifdngreop!", "encode", "caesar", 20) == "DCzxHALyIJ?"


def test_encode_3():
    assert do_operation("4$google_tengisahaha", "encode", "caesar", 100) == "9)lttlqj~yjslnxfmfmf"


def test_encode_4():
    assert do_operation("Very good story!", "encode", "vigenere", "Hello") == "{iCJnNszonZxzCM1"


def test_encode_5():
    assert do_operation("Do you hear me?", "encode", "vigenere", "No") == """;CMM"IMvRo%nZsq"""


def test_encode_6():
    assert do_operation("#78kjnchrnaE", "encode", "vigenere", "Abracadbra") == "{8oklnfiInAF"


def test_decode_1():
    assert do_operation("abc", "decode", "caesar", 3) == "89 "


def test_decode_2():
    assert do_operation("ERTdsffdvhuih5^&?827390", "decode", "caesar", 46) == "`8 !:##!=%<&%RFlAUOTPVM"


def test_decode_3():
    assert do_operation("dnfnooame 33", "decode", "caesar", 121) == "?}[}~~<|@;**"


def test_decode_4():
    assert do_operation("(fClq", "decode", "vigenere", "Abracadbra") == "Hello"


def test_decode_5():
    assert do_operation("""_sw*yqkFdTe:(HCs*nubvx2i"[Vdt~fLn""", "decode", "vigenere", "Het*arcneh1#%") ==\
                "Today is Monday and it`s so awful"


def test_decode_6():
    assert do_operation("""["TxBpvSsyJ"WxAd""", "decode", "vigenere", "INFjndhusk") == "Ooooomoyaoborona"


def test_encode_and_decode_1():
    encode_result = do_operation("Write me if u can", "encode", "caesar", 34)
    assert "Write me if u can" == do_operation(encode_result, "decode", "caesar", 34)


def test_encode_and_decode_2():
    encode_result = do_operation("123 is a Password!", "encode", "caesar", 45)
    assert "123 is a Password!" == do_operation(encode_result, "decode", "caesar", 45)


def test_encode_and_decode_3():
    encode_result = do_operation("Moijvmfzk04&62^^21", "encode", "caesar", 123)
    assert "Moijvmfzk04&62^^21" == do_operation(encode_result, "decode", "caesar", 123)


def test_encode_and_decode_4():
    encode_result = do_operation("Write me if u can", "encode", "vigenere", "abc")
    assert "Write me if u can" == do_operation(encode_result, "decode", "vigenere", "abc")


def test_encode_and_decode_5():
    encode_result = do_operation("123 is a Password!", "encode", "vigenere", "ahdejncuhdn")
    assert "123 is a Password!" == do_operation(encode_result, "decode", "vigenere", "ahdejncuhdn")


def test_encode_and_decode_6():
    encode_result = do_operation("Moijvmfzk04&62^^21", "encode", "vigenere", "%4$sdrQ^:")
    assert "Moijvmfzk04&62^^21" == do_operation(encode_result, "decode", "vigenere", "%4$sdrQ^:")


def test_caesar_break_1():
    assert do_operation(")zAMzAzMAN___", "caesar_break") == "I am a man!!!"


def test_caesar_break_2():
    assert do_operation(""""SBOVwAxVwIBxOKFKDw-VQELK""", "caesar_break") == "Every day learning Python"


def test_caesar_break_3():
    assert do_operation("!REzUzSUREzABOUTzIT9zrz4zrzbztd", "caesar_break") == "Are u sure about it: 2 + 2 = 4?"
