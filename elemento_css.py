from tkinter import Radiobutton
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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
driver.get('https://cursoautomacao.netlify.app/')

elemento_h2 = driver.find_element(By.CSS_SELECTOR, 'h2')
elemento_form_check = driver.find_element(By.CSS_SELECTOR, 'input[class="form-check-input"]')

if elemento_h2 is not None:
    print('Link home encontrado')
if elemento_form_check is not None:
    print('Link desafio encontrado')

input('')
driver.close()