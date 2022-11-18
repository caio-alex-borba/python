nome = {'nome':'','media':''}
nome['nome'] = str(input('Nome do aluno: '))
nome['media'] = float(input('media do aluno: '))
print('#'*30)
for i, a in nome.items():
    print(f'o {i} é {a}')
print('#'*30)
if nome['media'] >= 7:
    print(f'Aluno passado.')
if nome['media'] < 7:
    print('Aluno reprovado.')