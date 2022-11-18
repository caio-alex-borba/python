import pyperclip
import pyautogui
from time import sleep

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