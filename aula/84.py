nome = []
dado = []
sair = 'n'
gordo = []
magro = []
while True:
    nome.append(str(input('seu nome:')))
    nome.append(int(input('seu peso:')))
    dado.append(nome[:])
    nome.clear()
    sair = input('deseja continuar? S/N')
    if sair == 'n':
        break
for i in dado:
    if i[1] >= 50:
        gordo.append(i[0])
    elif i[1] <=49:
        magro.append(i[0])

print(f'Você cadastrou {len(dado)} pessoas.')
print(f'os mais pesados foram {gordo}')
print(f'E os mais leves foram {magro}')
