import pyautogui as pg

while True:
    a = pg.confirm('vc é bixa',buttons=['sim', 'nao'])
    if a == 'nao':
        a = pg.confirm('voce tem certeza',buttons=['sim', 'nao'])
        if a == 'sim':
            break
    if a == 'sim':
        break
