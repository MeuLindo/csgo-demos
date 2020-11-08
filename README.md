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
4. shell```python3 hltv_demo_downloader.py``` <- Esse cara precisa de um webdriver pro selenium funcionar, eu carreguei a versão do chrome, mas [aqui](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) tem pra outros navegadores.
---
### hltv-demos-scrap/hltv_demos/spiders/gerador_de_links.py:
* Entra em 'hltv.org/results' pega todos os links que tem 'matches' no href
* Append links achados em 'links_das_partidas.jl'
* Procura pelo link com a classe '.pagination-next'
* Pega todos os links que tem 'matches' no href na página nova
* Continua fazendo isso até '.pagination-next' não existir

### organizador_de_links_scrapados.py:
* Pega links_das_partidas.jl e transforma ele em um array
* Escreve essa lista nova em 'links_separados_todas_as_partidas_hltv.json'

### hltv_demo_downloader.py:
* Pega a lista de links scrapados e pega um por um e tenta baixar a demo
* Confere se a demo já terminou o download
* Pega o próximo link e repete o processo