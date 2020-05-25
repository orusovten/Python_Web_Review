from collections import defaultdict
import json
import string
import math


SYMBOLS_LIST = string.ascii_letters + string.punctuation + string.digits + " "
SYMBOLS_DICT = {char: index for index, char in enumerate(SYMBOLS_LIST)}


def shift_symbol(symbol, shift_size) -> str:
    index = SYMBOLS_DICT.get(symbol)
    if index is not None:
        return SYMBOLS_LIST[(index + shift_size) % len(SYMBOLS_LIST)]
    else:
        return symbol


def caesar_encode(line, step, sign) -> str:
    return "".join([shift_symbol(char, sign * step) for char in line])


def vigenere_shift(symbol, key_symbol, sign):
    return shift_symbol(symbol, sign * SYMBOLS_DICT[key_symbol])


def vigenere_encode(line, key_word, sign) -> str:
    return "".join([vigenere_shift(char, key_word[index % len(key_word)], sign) for index, char in enumerate(line)])


def encode(messages, cipher, key, sign):
    if cipher == "caesar":
        return caesar_encode(messages, int(key), sign)
    elif cipher == "vigenere":
        return vigenere_encode(messages, key, sign)


def count_freq(some_text):
    symbols_freq = defaultdict(int)
    for char in some_text:
        if char in SYMBOLS_DICT:
            symbols_freq[char] += 1
    return symbols_freq


def caesar_break(messages):
    with open("file_with_symbols_frequency.txt", "r") as freq_file:
        symbols_freq = json.load(freq_file)
    near_symbols_freq = count_freq(messages)
    min_difference = math.inf
    best_shift = 0
    for shift in range(len(SYMBOLS_LIST)):
        difference = 0
        for char in SYMBOLS_DICT:
            main_freq = symbols_freq.get(shift_symbol(char, shift))
            if main_freq is not None:
                difference += (near_symbols_freq[char] - main_freq) ** 2
        if difference < min_difference:
            min_difference = difference
            best_shift = shift
    return caesar_encode(messages, best_shift, 1)


def do_operation(text, operation, cipher="", key="") -> str:
    if operation == "decode":
        return encode(text, cipher, key, -1)
    if operation == "encode":
        return encode(text, cipher, key, 1)
    if operation == "caesar_break":
        return caesar_break(text)


def is_inside_alphabet(text) -> bool:
    for char in text:
        if char != "\n" and char not in SYMBOLS_DICT:
            return False
    return True


def find_errors_in_text(text):
    if text == "":
        return "Please, enter the text"
    if not is_inside_alphabet(text):
        return "{!r} is not consist of Alphabet symbols.".format(text)
    return ""


def find_errors_in_operation(operation, cipher="", key=""):
    if operation == "decode" or operation == "encode":
        if key == "":
            return "Please, enter the key.\n"
        if cipher == "caesar":
            try:
                int(key)
            except ValueError:
                return "Please, enter the number key.\n"
        elif cipher == "vigenere":
            if not is_inside_alphabet(key):
                return "Please, enter the key in Alphabet.\n"
    return ""
