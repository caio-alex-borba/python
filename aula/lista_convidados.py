from termcolor import colored

lista_nomes = []
numero_convidados = input(colored('numero de convidados: ', 'red'))

while len(lista_nomes) < int(numero_convidados):
    lista_nomes.append(input(colored('nomes dos convidados: ', 'blue')))

print('sao',numero_convidados,'convidados, sendo eles')
for i in lista_nomes:
    print(i)










