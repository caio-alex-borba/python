cad = []
while True:
    try:
        print('-' * 20)
        print(f'{"MENU":^10}')
        print('1- cadastrar\n2- ver lista\n3- sair')
        print('-' * 20)
        menu = int(input('opção: '))
        temp = open('lista.txt', 'a')
        if menu == 1:
            print("-"*20)
            print(f'{"CADASTRAR":^15}')
            nome = str(input('nome: '))
            idade = int(input('idade: '))
            temp.write(f'{nome};{idade}\n')

        if menu == 2:
            print('-'*20)
            print(f'{"LISTA":^15}')
            cadastro2 = open('lista.txt','rt')
            for i in cadastro2:
                dado = i.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<}{dado[1]:>10}')
        if menu == 3:
            break

    except (ValueError, TypeError):
        print('opção invalida')
    except KeyboardInterrupt:
        break
    finally:
        print()
        print('-'*20)
        print('\nObrigado, volte sempre')


