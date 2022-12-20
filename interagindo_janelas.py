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
sleep(2)
janela_inicial = driver.current_window_handle
driver.execute_script('window.scrollTo(0, 2500)')
sleep(2)
botao_abrir_nova_janela = driver.find_element(
    By.XPATH, "//button[text()='Abrir nova janela']")
sleep(2)
driver.execute_script('arguments[0].click()', botao_abrir_nova_janela)
janelas = driver.window_handles

for janela in janelas:

    if janela not in janela_inicial:
        driver.switch_to.window(janela)
        sleep(2)
        campo_pesquisa = driver.find_element(By.XPATH, "//textarea[@class='form-control']")
        sleep(2)
        campo_pesquisa.send_keys("O curso está maravilhoso!")
        sleep(2)
        botao_pesquisar = driver.find_element(By.XPATH, "//button[@id='fazer_pesquisa']")
        sleep(2)
        botao_pesquisar.click()
        driver.close()

driver.switch_to.window(janela_inicial)
campo_mensagem = driver.find_element(By.XPATH, "//textarea[@id='campo_desafio7']")
sleep(2)
campo_mensagem.send_keys("consegui!")

input('')
driver.close()
