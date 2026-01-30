from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By 
from time import sleep

# Configurar o caminho para o ChromeDriver na pasta de rede comando do google web
chrome_driver = r"C:\Users\edmil\Downloads\chromedriver_win32\chromedriver.exe"

# Configurar as preferências do Chrome para salvar automaticamente os downloads na pasta de destino
pasta_destino = r"C:\Users\edmil\OneDrive\Documentos\Dpersonalizado"

preferencias = {
    "download.default_directory": pasta_destino
    
}

# Configurar as opções do Chrome
options = ChromeOptions()
options.add_experimental_option("prefs", preferencias) # adicinar preferencias 
options.headless = False                               # Mostrar navegador ao executar automação headless = False   mostrar navegador headless = True Não mostrar o navegador   

# Configurar serviço do ChromeDriver
chrome_service = ChromeService(executable_path=chrome_driver)

# Instanciar o navegador Chrome passando o Service e as opções
navegador = webdriver.Chrome(service=chrome_service, options=options)

# Agora o Chrome será iniciado a partir do executável do Chrome Portable e controlado pelo ChromeDriver.
Link = "https://rpachallenge.com/"
navegador.get(Link)



# %%
sleep(5)
Baixar =    navegador.find_element(by= By.XPATH,value='/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a').click()


