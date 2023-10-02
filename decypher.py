import utilites
def decrypet(encrypeted, key):
    plain_text = ''
    matrix = utilites.vigenereMatrix()

    suitable_key = utilites.trim(encrypeted, key)
    encrypeted_len = len(encrypeted)

    for i in range(encrypeted_len):
        key_line = utilites.alphabetDict(suitable_key[i])
        looking_letter = encrypeted[i]

        row = 0

        while matrix[key_line][row] != looking_letter:
            row += 1

        plain_text = plain_text + matrix[0][row]

    return plain_text

