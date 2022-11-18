import pandas as pd
import pyperclip
import pyautogui
from time import sleep
from IPython.display import display
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(1)
pyautogui.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=331, y=285, clicks=2)
sleep(3)
pyautogui.click(x=331, y=285)
sleep(3)
pyautogui.click(x=1149, y=189)
sleep(3)
pyautogui.click(x=919, y=591)
sleep(8)

tabela = pd.read_excel(r"D:\dowlodes\Vendas - Dez.xlsx")

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()


pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('gmail.com')
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=117, y=215)
sleep(3)
pyautogui.write('caio.alex.borba@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('tabela de vendas')
pyautogui.press('tab')
pyautogui.write(f'faturamento total de R${faturamento:,.2f}\n'
                f'E total de produtos foi {quantidade:,}.')
pyautogui.hotkey('Ctrl', 'enter')
