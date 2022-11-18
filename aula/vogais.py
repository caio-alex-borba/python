lis = ('casa', 'rua', 'predio', 'loja', 'mercado')

for i in lis:
    print(f'\nna palavra {i} temos ',end='')
    for letra in i:
        if letra in 'aeiou': # cada loop da tuple ele procura a letra na palavra
            print(letra,end=' ')