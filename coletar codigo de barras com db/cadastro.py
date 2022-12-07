import cv2 as cv
from pyzbar.pyzbar import decode
import sqlite3
from time import sleep



def Camera():
    camera = cv.VideoCapture(0)
    rodando = True
    while rodando:
        status, frame = camera.read()
        if not status or cv.waitKey(1) & 0xff == ord('q'):
            rodando = False
        cv.imshow("Camera", frame)
        codigo = decode(frame)
        if not codigo: 
            print("Barcode Not Detected or your barcode is blank/corrupted!")
            sleep(2)
        else: 
            for barcode in codigo:   
                (x, y, w, h) = barcode.rect 
                cv.rectangle(frame, (x-10, y-10), 
                (x + w+10, y + h+10),  
                (255, 0, 0), 2) 
                if barcode.data !="": 
                    rodando = False
                    codigo = int(barcode.data)
                    return codigo
                    
        
    #cv.imshow("Image", frame)
    #cv.waitKey(0)# 
    #cv.destroyAllWindows()#

def Add_banco(codigo,produto):
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()

    cria_tabela = "CREATE TABLE IF NOT EXISTS produtos (codigo INTEGER, produto text)"

    add = f"INSERT INTO produtos VALUES ('{codigo}','{produto}')"

    cursor.execute(cria_tabela)
    cursor.execute(add)

    conexao.commit()
    conexao.close()

def List():
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    listar = "SELECT * FROM produtos"
    cursor.execute(listar)
    tabela = []
    for linha in cursor.fetchall():
        tabela.append(f'{linha[0]}--{linha[1]}')

    conexao.commit()
    conexao.close()
    return tabela


ops = 0
while ops != 3:
    print('1= cadastrar')
    print('2= listar')
    print('3= Finalizar')
    print()
    ops = int(input('Selecione uma opção: '))
    print()
    print()
    if ops == 1:
        codigo = Camera() 
        print('Coletando Codigo De Barras')
        sleep(2)
        print(codigo)
        produto = str(input('Produto: '))
        sleep(2)
        Add_banco(codigo, produto)
        print(f'{codigo}:{produto}')
        print()
        print()
        continue
    if ops == 2:
        lista = List()
        print('Consultando Lista...')
        sleep(2)
        print(lista)
        print()
        print()
        cont = 0
        cont = int(input('Digite 1 para voltar: '))
        if cont == 1:    
            continue

    
