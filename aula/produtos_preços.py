pro = ('caderno', 3.50,
       'lapiz', 1.50,
       'caneta', 2.50,
       'borracha', 1.10,
       'lapizeira', 3.50)
for i in range(len(pro)):
    if i % 2 == 0:
        print(f'{pro[i]:.<30}',end='')
    else:
        print(f'R${pro[i]:>5.2f}')
