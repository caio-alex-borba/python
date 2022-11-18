from pyautogui import confirm

while True:
    a = confirm('vc é bixa',buttons=['sim', 'nao'])
    if a == 'nao':
        a = confirm('vc é bixa', buttons=['nao', 'sim'])
    if a == 'sim':
        confirm('BIXOOOONA')
        break
