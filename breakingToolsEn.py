from sys import maxsize
import string

# Map with letters corresponding indexes
# The letters are the keys and the values are the frequencies
# These numbers are the standard frequencies of the letters of the english alphabet

en_freq = {'a': 0.0817,
           'b': 0.0149,
           'c': 0.0278,
           'd': 0.0425,
           'e': 0.1270,
           'f': 0.0223,
           'g': 0.0202,
           'h': 0.0609,
           'i': 0.0697,
           'j': 0.0015,
           'k': 0.0077,
           'l': 0.0403,
           'm': 0.0241,
           'n': 0.0675,
           'o': 0.0751,
           'p': 0.0193,
           'q': 0.0010,
           'r': 0.0599,
           's': 0.0633,
           't': 0.0906,
           'u': 0.0276,
           'v': 0.0098,
           'w': 0.0236,
           'x': 0.0015,
           'y': 0.0197,
           'z': 0.0007}

en_index_of_coincidence = 0.067


# this method attempts to find the length of the key
def key_size(encripeted, max_key_len):
    min_diff = maxsize
    key_len = 0

    for candidate_length in range(1, max_key_len + 1):
        groups, last_group = get_blocks(text=encripeted, size=candidate_length)
        columns, last_column = get_columns(groups, last_group)
        ics = [coincidence_index(letter_counter=get_Letter_Counts(encripeted=column)) for column in columns]
        delta_bar_ic = sum(ics) / len(ics)

        if en_index_of_coincidence - delta_bar_ic < min_diff:
            min_diff = en_index_of_coincidence - delta_bar_ic
            key_len = candidate_length

    return key_len

def coincidence_index(letter_counter):
    numerator = sum([letter_counter[l] * (letter_counter[l] - 1) for l in string.ascii_lowercase])
    text_size = sum(occurrences for occurrences in letter_counter.values())
    denominator = text_size * (text_size - 1)

    return numerator / denominator


# This function splits the ciphettext into blocks and
# creates a list of substrings whose length equals to the block's length (size)
def get_blocks(text, size):
    # size is the block's length
    blocks = [text[i:i + size] for i in range(0, len(text) - size, size)]

    last_block = text[len(text) % size + len(text) - size:]

    return blocks, last_block


# This function separates the ciphertext into columns and each column has the size of it's block
def get_columns(text_blocks, last_block=''):
    group_size = len(text_blocks[0])
    columns = []
    last_column = []

    for letter_count in range(group_size):
        column = ''

        for group_count in range(len(text_blocks)):
            column += text_blocks[group_count][letter_count]

        columns.append(column)
        last_block_list = list(last_block)

        # Append last block of the list to the last column if length of the last block is bigger than the letter's position in the alphabet
        if len(last_block_list) > letter_count:
            last_column.append(last_block_list[letter_count])

    # Returns the ciphertext in columns
    return columns, last_column

def get_Letter_Counts(encripeted):
    # letter counter
    letter_counts_array = {}

    for index, letter in enumerate(string.ascii_lowercase):
        letter_counts_array[letter] = encripeted.count(letter)

    return letter_counts_array


# This function calculates the frequency of each character found in the ciphertext
def letter_frequencies(text):
    letter_counts = get_Letter_Counts(text)

    # for each key=letter and value=count compute the frequency of each letter
    frequencies = {letter: count / len(text) for letter, count in letter_counts.items()}

    return frequencies


# Makes right shift of the ciphertext
def shift(text, amount):
    letters = string.ascii_lowercase
    shifted = ''

    for letter in text:
        shifted += letters[(letters.index(letter) - amount) % len(letters)]

    return shifted


# Correlation function
def correlation(text, lf):
    return sum([(lf[letter] * en_freq[letter]) for letter in text])


# This function calculates each letter of the ciphertext's key
def find_letter_key(text, lf):
    letter_key = ''
    max_cor = 0

    for count, letter in enumerate(string.ascii_lowercase):
        shifted = shift(text=text, amount=count)
        cor = correlation(text=shifted, lf=lf)

        if cor > max_cor:
            max_cor = cor
            letter_key = letter

    return letter_key


# this method find the actual key
def key_refactor(encripeted, key_len):
    key = ''
    blocks, last_block = get_blocks(text=encripeted, size=key_len)
    columns, last_column = get_columns(blocks, last_block)
    frequencies = letter_frequencies(text=encripeted)

    counter = 1
    for column in columns:
        key += find_letter_key(text=column, lf=frequencies)
        counter += 1

    return key
