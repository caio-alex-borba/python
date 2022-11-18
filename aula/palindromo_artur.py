print('Seja bem-vindo!!!')
frase = str(input('Frase do dia: ')).replace(' ','')
frase = frase.lower()
b = len(frase)
for c in range(0, b - 1):
    #print(f'{frase[(b -1) - (c)]} {b} eeee {frase[c]} {c}')
    if frase[(b - 1) - c] != frase[c]:
        b = 0
        if c == 0:
            frase == str('abc')
            print('Sua frase não é \033[4;34mpalindroma\033[m')
    elif frase[(b - 1) - c] == frase[c]:
        if b != 0 and c == 0:
            print('Sua frase é \033[4;34mpalindroma\033[m!!!')
        #print(f'{frase[(b -1) - (c)]} {b} eeee {frase[c]} {c}')