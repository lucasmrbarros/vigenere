plain_text = 'Mankeskin'
key = 'ita'

def decrypet(encrypeted, key):
    plain_text = 'not implemented just yet'
    return plain_text


#this function allows to make the key length matches the plain text length
def trim(plain_text, key):
    suitable_key = ''

    plain_text_lenght = len(plain_text)

    print('Lunghezza del plain text', plain_text_lenght)

    for i in range(plain_text_lenght):
        suitable_key = suitable_key + key

    suitable_key = suitable_key[:plain_text_lenght]

    return suitable_key

def matrix():
    matrix = []
    for i in range(26):
        matrix.append([])
        for j in range(26):
            letra = chr(((i + j) % 26) + ord('A'))
            matrix[i].append(letra)
    return matrix