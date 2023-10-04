import cypher, decypher, breaking
import  re

exit_flag = 0

while exit_flag == 0:
    print('________________________________')
    print('Qual operação deseja executar? ')
    print('1 - Cifração')
    print('2 - Decifração')
    print('3 - break the law')
    print('0 - Sair')

    choice = input()
    choice = int(choice)

    if choice == 1:
        print('Digite o texto a ser cifrado:')
        plain_text = input()
        plain_text = re.sub(r'[^a-z\n]', '', plain_text.lower())

        print('Digite a chave: ')
        key = input()
        key = str(key).lower()

        encrypted = cypher.encrypet(plain_text, key)
        print('Texto cifrado: ', encrypted)

    elif choice == 2:
        print('Digite o texto criptografado: ')
        encrypted_text = input()
        encrypted_text = re.sub(r'[^a-z\n]', '', encrypted_text.lower())

        print('Digite a chave: ')
        key = input()
        key = str(key).lower()

        plain_text = decypher.decrypet(encrypted_text, key)
        print('A mensagem original é: ', plain_text)

    elif choice == 3:
        print('Digite o texto que cripotografado que deseja quebrar: ')
        encrypted_text = input()
        encrypted_text = re.sub(r'[^a-z\n]', '', encrypted_text.lower())

        print('Valores muito distantes ou menores do tamanho da chave geram inconsistências')
        print('Informe o tamanho maximo da chave: ')

        max_key_len = int(input())

        print('Selecione o idioma para tentar o ataque:')
        print('1- portugues')
        print('2- Inglês')

        lenguage = int(input())

        key = breaking.breakingTheLaw(encrypted_text, max_key_len, lenguage)
        print('A chave é: ', key)

    elif choice == 0:
        exit_flag = 1
