import scrapy
from scrapy import Request


class CandidatosSpider(scrapy.Spider):
    name = "candidatos"

    def start_requests(self):
        initial_year = 2014
        url = 'https://www.tse.jus.br/hotsites/pesquisas-eleitorais/candidatos_anos/{}.html'
        for year in range(initial_year, 2022, 2):
            yield Request(url=url.format(str(year)), callback=self.parse, meta={'name': str(year) + '.zip'})

    def parse(self, response):
        filename = response.request.meta['name']
        file_url = response.xpath('//div[@class= "prepend-1"]//a/@href').get()
        yield {
            "filename": filename,
            "file_urls": [file_url]
        }
