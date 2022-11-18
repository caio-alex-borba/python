n = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze',
     'doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    num = int(input('digite um numero entre 0 e 20\n'))
    if 0 <= num <= 20:
        break
num = n[num]
print(num)
