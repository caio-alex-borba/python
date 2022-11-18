import requests
real = float(input('Digite quantos dolares voce quer compra? USD$:'))
url = 'https://economia.awesomeapi.com.br/all/USD-BRL' # link publico com o valor atual

response = requests.get(url) # busca os dados

if response.status_code == 200: # se a busca funcionol vai mostrar o valor
    dolar_valor = float(response.json()['USD']['low'])

print(f'Com a cotação do dolar de hoje em R$:{dolar_valor:.2f}, voce vai pagar R$:{dolar_valor * real:.2f}')
