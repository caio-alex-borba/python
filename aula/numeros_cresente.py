num = list()
while True:
    n = int(input('digite um numero: '))
    if n not in num:
        num.append(n)
    else:
        print('numero ja existente')
    r = str(input('deseja continiar? S/N: '))
    if r in 'nN':
        break
print(sorted(num))