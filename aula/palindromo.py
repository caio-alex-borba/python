print('TESTE DE PALINDROMO')

frase = str(input('frase do dia: ')).strip()  # retira o espaço do inicio e fim
frase = frase.lower()                         # formata a frase para minuscula
frase = frase.replace(' ', '')                        # remove o espaço no meio da frase

a = frase[::-1]                               # redigita a frase de tras para frente

if frase == a:
    print('esta frase é um palindromo.')
else:
    print(f'esta frase nao é um palindromo.')