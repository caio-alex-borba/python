
n = int(input('digite um numero '))
if n == 2:
    print('numero primo')
for a in range(2, n):
    b = n / a
    c = b.is_integer()
    if c == True:
        if a < n:
            n = 0
            print(f'seu numero não é primo')
    elif c == False and a == n - 1:
        print(f'{n} é um numero primo')