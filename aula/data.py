from datetime import datetime
d = int(datetime.today().strftime('%d%m%y'))
h = datetime.today().strftime('%H:%M')
pess = int(input('sua data de nacimento D-M-A'))
idae = pess-d
print(idae)
