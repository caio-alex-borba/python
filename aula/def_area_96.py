def area(a, b):
    """

    :param a: comprimento
    :param b: largura
    :return: area do tereno
    """
    c = a*b
    print(f'A area de um terreno {a}x{b} é {c:.2f}M².')


area(float(input('comprimento: ')), float(input('largura: ')))
