def dobro(m=0):
    m *= 2
    return (f'R${m:.2f}'.replace('.',','))
def metade(m=0):
    m /= 2
    return (f'R${m:.2f}'.replace('.',','))
def aumento(m=0, j=0):
    a = m + (j/100*m)
    return (f'R${a:.2f}'.replace('.',','))
def diminuir(m=0, j=0):
    a = m - (j/100*m)
    return (f'R${a:.2f}'.replace('.',','))
def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
def resumo(preço=0, d=0, j=0):
    print('#'*30)
    print('resumo'.center(30))
    print('#'*30)
    print(f'Valor analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço)}')
    print(f'Metade do preço: \t{metade(preço)}')
    print(f'{j}% de juros: \t\t{aumento(preço, j)}')
    print(f'{d}% de redução: \t{diminuir(preço, d)}')
    print('#'*30)