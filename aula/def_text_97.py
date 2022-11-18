def texto(txt):
    a = len(txt)+4
    print('#' * a)
    print(f'  {txt}')
    print('#' * a)

texto(input('mensagem: '))

