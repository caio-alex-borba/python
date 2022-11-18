cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['nacimento'] = int(input('Data de nacimento: '))
cadastro['clt'] = int(input('Registro de trabalho 0 se for desempregado: '))
if cadastro['clt'] != 0:
    cadastro['contrato'] = int(input('Ano de contratação: '))
    cadastro['salario'] = int(input('Salario: '))
    print('#'*20)
    for i, v in cadastro.items():
        print(f'{i}: {v}')
    idade = 2022 - cadastro['nacimento']
    print(f'idade: {idade} anos')
    apo = 50 - (2022 - cadastro['contrato'])
    print(f'Aposentadoria: {apo+idade} anos')

elif cadastro['clt'] == 0:
    print(cadastro)
