import os, time, json
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

driver = Chrome('/home/meulindx/selenium/tutorial/chromedriver.exe')

hltv_root = 'https://www.hltv.org'
f = open('links_separados_todas_as_partidas_hltv.json',)
todas_as_partidas_urls = json.load(f)
todas_as_partidas_urls.pop(0) # primeiro index é só /matches
partidas_baixadas = []

for partida in todas_as_partidas_urls:
    driver.get(hltv_root + partida)
    time.sleep(10)
    partidas_baixadas = todas_as_partidas_urls.pop(0)
    print(hltv_root + partida)
    
    gotv_demo = driver.find_element_by_css_selector('body > div.bgPadding > div > div.colCon > div.contentCol > div.match-page > div.g-grid.maps > div.col-6.col-5-small > div > div:nth-child(1) > a')
    gotv_demo.click()

    time.sleep(20)
    
    wait = True
    while wait:
        lista_de_arquivos = os.scandir('/mnt/c/Users/alexa/Downloads')
        counter = 0
        for arquivo in lista_de_arquivos:
            if '.crdownload' in str(arquivo):
                print(f'Baixando: {partida}')
                counter += 1
            else:
                pass
        if counter > 0:
            wait = True
            time.sleep(10)
        else:
            wait = False
            print('Partida baixada.')

driver.quit()