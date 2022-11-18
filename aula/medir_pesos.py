peso = [input('digite seu peso')]
       # len em lista conta os itens
while len(peso) < 5:
    peso.append(input('digite seu peso'))

print(f'\nO maior peso é {max(peso)} e o menor peso é {min(peso)}')
                          # max da o mair valor        #min da o menor valor