def nota(*num, situ=False):
    n = {}
    n['total'] = len(num)
    n['maior'] = max(num)
    n['menor'] = min(num)
    n['media'] = sum(num) / len(num)
    if situ:
        if n['media'] >= 7:
            n['situação'] = 'boa'
        elif n['media'] >= 5:
            n['situação'] = 'razoavel'
        else:
            n['situação'] = 'ruim'
    return n


notas = nota(2, 10, 10, 10, 10, situ=True)
print(notas)
