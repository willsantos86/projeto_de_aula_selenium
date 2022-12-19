from tabnanny import check
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1400,1050', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()


# navegar até o site
driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(5)
driver.execute_script("window.scrollTo(0, 1600)")
sleep(2)
carros = checkboxes = driver.find_elements(By.XPATH, "//input[@name='carros']")
motos = checkboxes = driver.find_elements(By.XPATH, "//input[@name='motos']")

carros[1].click()
carros[3].click()
carros[4].click()

sleep(2)

for moto in motos:
    moto.click()

    


input('')
driver.close()
