import scrapy
from scrapy import Request


class CandidatosSpider(scrapy.Spider):
    name = "candidatos"

    def start_requests(self):
        initial_year = 1994
        url = 'https://www.tse.jus.br/hotsites/pesquisas-eleitorais/candidatos_anos/{}.html'
        for year in range(initial_year, 2022, 2):
            yield Request(url=url.format(str(year)), callback=self.parse)

    def parse(self, response):
        file_url = response.xpath('//div[@class= "prepend-1"]//a/@href').get()
        yield {
            "file_urls": [file_url]
        }
