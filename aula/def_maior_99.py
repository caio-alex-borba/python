def maior(* núm):
    cont = maior = 0
    print('\nverificando os valores...')
    for i in núm:
        cont +=1
        print(i,end=' ')
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
    print(f'Foram informados {cont} valores.')
    print(f'o maior valor foi {maior}')

maior(9, 6, 7)
