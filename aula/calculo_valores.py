from termcolor import colored
Valor = float(input('Valor: '))
Pagamento = str(input('forma de pagamento: '))
Pagamento = Pagamento.title()
Pagamento = Pagamento.strip()

if Pagamento == "Dinheiro" or Pagamento == "Cheque":
    print(f'Você deve pagar{Valor - (Valor * 10/100)}')
elif Pagamento == 'Cartao' or Pagamento == 'Cartão':
    car = str(input('Avista ou Parcelado? '))
    car = car.title()
    car = car.strip()
    if car == 'Avista':
        print(f'Você vai pagar {Valor - (Valor * 5/100)}')
    elif car == 'Parcelado':
        parc = int(input('Em quantas vezes? '))
        if parc <= 2:
            print(f'Você vai pagar {Valor} em {parc}x de {Valor / parc}')
        else:
            print(f'Você vai pagar {20 / 100 * Valor + Valor}x em {parc} de {Valor/parc}')






