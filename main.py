import cypher, decypher, breaking

exit_flag = 0

while exit_flag == 0:
    key = ''
    encrypted_text = ''
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
        plain_text = ''
        input(plain_text)

        print('Digite o texto a chave: ')
        input(key)

        encrypted = cypher.encrypet(plain_text, key)
        print('Texto cifrado: ', encrypted)

    elif choice == 2:
        print('Digite o texto criptografado: ')
        input(encrypted_text)
        print('Digite a chave: ')
        input(key)

        plain_text = decypher.decrypet(encrypted_text, key)
        print('A mensagem original é: ', plain_text)

    elif choice == 3:
        print('Digite o texto que cripotografado que deseja quebrar: ')
        input(encrypted_text)

        key = breaking.breakingTheLaw(encrypted_text)
        print('A chave é: ',key)

    elif choice == 0:
        exit_flag = 1