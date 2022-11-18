from datetime import date
import time
fut = int(input('Quantos anos vou ter em '))
time.sleep(1)
anos = int(input('Quantos anos você tem? '))
hoje = date.today().year
idade = hoje - anos
futuro = fut - idade
time.sleep(3)
print('PERA QUE TO PENSANDO')
time.sleep(2)
print(f'Voce naceu em {idade}, com isso em {fut} você tera {futuro}')
