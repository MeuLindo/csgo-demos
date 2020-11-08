# CSGO Demos
---
## Dependências:
    -json
    -json_lines
    -selenium
    -scrapy
---
## Workflow:
1. hltv-demos-scrap/
2. shell```scrapy crawl gerador_de_links``` <- Arquivo gerado: 'links_das_partidas.jl'
3. shell```python3 organizador_de_links_scrapados.py``` <- Arquivo gerado: 'links_separados_todas_as_partidas_hltv.json'
4. shell```python3 hltv_demo_downloader.py``` <- Esse cara precisa de um webdriver pro selenium funcionar, eu carreguei a versão do chrome, mas [nesse](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) link tem pra outros navegadores.
---
### hltv_demo_downloader.py:
* Pega a lista de links scrapados e pega um por um e tenta baixar a demo
* Confere se a demo já terminou o download
* Pega o próximo link e repete o processo
