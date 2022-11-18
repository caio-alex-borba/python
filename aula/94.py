lista = []
media = []
mulher = []
while True:
    pess = {}
    pess['nome'] = str(input('seu nome: '))
    pess['sexo'] = str(input('F para feminino / M para masculino: ')).upper()
    pess['idade'] = int(input('sua idade: '))
    lista.append(pess)
    media.append(pess['idade'])
    if pess['sexo'] == 'F':
        mulher.append(pess['nome'])
    if input('dseja continuar: ') == 'n':
        break
media = sum(media) / len(lista)
acmed = []
for i in lista:
    if i['idade'] > media:
        acmed.append(i['nome'])
print()
print('#'*30)
print(f'Foi cadastrado {len(lista)} pessoas.')
print(f'A media de idade do grupo foi {media} anos.')
print(f'Mulheres: {mulher}')
print(f'Idade acima da media: {acmed}')
