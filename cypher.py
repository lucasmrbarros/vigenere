import utilites


def encrypet(plain_text, key):
    cypher_text = ''
    matrix = utilites.vigenereMatrix()

    suitable_key = utilites.trim(plain_text, key)
    plain_text_len = len(plain_text)

    for i in range(plain_text_len):
        line = utilites.alphabetDict(suitable_key[i])
        row = utilites.alphabetDict(plain_text[i])

        cypher_text = cypher_text + matrix[line][row]

    return cypher_text
