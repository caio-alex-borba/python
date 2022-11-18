from selenium import webdriver

nav = webdriver.Chrome()
nav.get('https://www.climatempo.com.br/')

card = nav.find_elements(by=id('current-weather-temperature'))

print(card)