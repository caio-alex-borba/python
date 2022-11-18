usuario = input('equação')
a = usuario.count('(')
b = usuario.count(')')
c = (a + b) / 2
d = c.is_integer()
if d == True:
    print(f"sua equação esta utilizando corretamente os parênteses")
else:
    print('infelizmente você não utilizou os parênteses corretamente')
