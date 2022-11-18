num = list()
max = 0
min = 0
for c in range(0, 5):
    num.append(int(input(f'digite um numero para a posição {c}: ')))
    if c == 0:
        max = min = num[c]
    else:
        if num[c] > max:
            max = num[c]
        if num[c] < min:
            min = num[c]
print(f'Você digitou {num}')
print(f'O maior foi {max} na posição ',end='')
for i, v in enumerate(num): #posição que aparece
    if v == max:
        print(f'{i}--- ',end='')
print()
print(f'O menor foi {min} na posição ',end='')
for i, v in enumerate(num):
    if v == min:
        print(f'{i}--- ',end='')
print()