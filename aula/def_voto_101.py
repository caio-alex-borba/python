def voto(a):
    """
    Calcula se a pessoa tem direito de voto.
    :param a: Ano de nacimento.
    :return: a possibilidade de voto.
    """
    from datetime import date
    data = date.today().year
    a = data - a
    if a < 16:
        return f'{a}: voto negado.'
    elif 16 <= a < 18 or a > 65:
        return f'{a}: voto opcional.'
    else:
        return f'{a}: voto obrigatorio.'


pessoa = voto(int(input('Data de nacimento: ')))
print(pessoa)