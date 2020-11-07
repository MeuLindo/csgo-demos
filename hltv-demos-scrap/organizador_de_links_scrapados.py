import json_lines
import json

todas_as_paginas = []

with open("links_das_partidas.jl", 'rb') as f:
    for item in json_lines.reader(f):
        todas_as_paginas.append(item)

links_separados = []

for pagina in todas_as_paginas:
    for link in pagina[0]:
        links_separados.append(link)

print(len(links_separados))

for i in range(10):
    print(links_separados[i])

with open('links_separados_todas_as_partidas_hltv.json', 'w', encoding='utf-8') as f:
    json.dump(links_separados, f, ensure_ascii=False, indent=4)
    