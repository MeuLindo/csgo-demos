import scrapy
import json
import jsonlines

class GeradorDeLinksSpider(scrapy.Spider):
    name = "gerador_de_links"
    start_urls = ["https://www.hltv.org/results"]
    

    def parse(self, response):
        links_das_partidas = []
        links_das_partidas.append(response.xpath('//a[contains(@href, "matches")]/@href').getall())
        
        next_page = response.css("a.pagination-next::attr(href)").get().split("results")[1]
        offset = int(next_page.split('=')[1])
        limite = 5000000

        if (offset < limite) and next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        # with open('links_partidas_hltv.json', 'w') as f:
        #     json.dump(links_das_partidas, f)
        
        with jsonlines.open('links_das_partidas.jl', mode='a') as writer:
            writer.write(links_das_partidas)