import requests

url = 'https://economia.awesomeapi.com.br/all/USD-BRL' # link publico com o valor atual

response = requests.get(url) # busca os dados

if response.status_code == 200: # se a busca funcionol vai mostrar o valor
    dolar_valor = float(response.json()['USD']['low'])
    print(f'valor do dolar em R$: {dolar_valor}')
else:
    print('erro')