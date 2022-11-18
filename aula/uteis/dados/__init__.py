def validador(msg):
    while True:
        valor = str(input(msg)).strip()
        if valor.isalpha() or valor == '':
            print(f'{valor} não é um VALOR valido')
        else:
            break
    return float(valor.replace(',','.'))

def testsite(msg):
    from urllib import request
    try:
        ste = request.urlopen(f'https://www.{msg}.com/')
    except:
        print('o site nao esta ativo no momento')
    else:
        print('o site esta funcionando normalmente.')

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('eeror na abertura do aquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na gravação do arquivo')
        else:
            print(f'novo nome {nome} cadastrado')
            a.close()
