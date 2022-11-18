lista = []
while True:
    aluno = str(input('Nome do aluno: '))
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    media = (nota1+nota2) / 2
    lista.append([aluno,[nota1,nota2],media])
    if input('Deseja continuar? S/N: ') == 'n':
        break
print('#'*22)
print(f'{"No°":<4}{"nome":^10}{"Media":>8}')   #print formatado
for i, e in enumerate(lista):
    print(f'{i:<4}{e[0]:^10}{e[2]:>8.1f}')
print()
while True:
    p = int(input('Deseja ver as notas de qual aluno? 99 para sair. N°: '))
    if p == 99:
        break
    if p <= len(lista) -1:
        print(f'As notas de {lista[p][0]} são {lista[p][1]}')
    print()
