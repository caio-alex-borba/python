from termcolor import colored
print(colored('formulario exercito\n','red'))

nome = input('seu nome: ')
idade = input('sua idade: ')
altura = input('sua altura: ')
peso = input('seu peso: ')

if idade >= '18' and altura >= '1,50' and peso >= '50':
    print('\nvocê',colored(nome,'green'),'esta apto para o trabalho')

else:
    print('\nvocê',colored(nome,'red'),'esta inapto para o trabalho')