#this function allows to make the key length matches the plain text length
def trim(plain_text, key):
    suitable_key = ''

    plain_text_lenght = len(plain_text)

    for i in range(plain_text_lenght):
        suitable_key = suitable_key + key

    suitable_key = suitable_key[:plain_text_lenght]

    return suitable_key

#this function converts the letter to the alphabetic numer  and vice-versa
def alphabetDict(value):
    alphabet_to_number = {lettera: indice for indice, lettera in enumerate('abcdefghijklmnopqrstuvwxyz')}

    return alphabet_to_number[value]

#This function build the matrix used to encrypt and also decrypt
def vigenereMatrix():
    matrix = []
    for i in range(26):
        matrix.append([])
        for j in range(26):
            letra = chr(((i + j) % 26) + ord('A'))
            matrix[i].append(letra)
    return matrix
#this function just print the matrix, can be use to do some debugging
def printVigenereMatrix(matrix):
    for line in matrix:
        for letter in line:
            print(letter, end=' ')
        print()
#x = vigenere_matrix()
#print_vigenere_matrix(x)


