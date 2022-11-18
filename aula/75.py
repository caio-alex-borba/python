num = (int(input('digite um numero: ')),
       int(input('digite mais um: ')),
       int(input('digite outro: ')),
       int(input('so mais um:')))
a = 0
p = 0
for i in num:

    if i == 9:
        a += 1
for i in num:
    if i % 2 == 0: # % 2 == 0 se for 0 é par se for 1 é impar
        p += 1

print(f'voce digitou {num} O numero 9 aparece {a} vezes.\n'
      f'O numero 3 apareceu na posição {num.index(3)}.\n'
      f'E os numeros pares forão {p}.')



