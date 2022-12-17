from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


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

# navegar até o site
driver.get('https://cursoautomacao.netlify.app/')
sleep(3)
# encontrar e clickar no link de login
botao_login = driver.find_element(By.LINK_TEXT, 'Login')
sleep(1)
botao_login.click()
sleep(1)
# encontrar e clickar no link senha
campo_email = driver.find_element(By.NAME, 'email')
sleep(1)
# Digitar semail (login)
campo_email.send_keys('willsantos.edf@gmail.com')
sleep(1)
# encontrar minha senha
campo_senha = driver.find_element(By.ID, 'senha')
sleep(1)
# digitar senha
campo_senha.send_keys('#Willi@m86')
sleep(1)
# encontrar e clickar no botão enviar
botao_enviar = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
sleep(1) 
botao_enviar.click()

input('')
driver.close()
