def testsite(msg):
    from urllib import request
    try:
        ste = request.urlopen(f'https://www.{msg}.com/')
    except:
        print('o site nao esta ativo no momento')
    else:
        print('o site esta funcionando normalmente.')
