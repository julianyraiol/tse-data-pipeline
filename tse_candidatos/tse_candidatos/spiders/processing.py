
import scrapy
from scrapy import Request
from glob import glob
from pathlib import Path
from zipfile import ZipFile


class UnzipFilesSpider(scrapy.Spider):
    name = 'processing'

    def __init__(self):
        self.start_urls = glob('data/*.zip')

    def start_requests(self):
        for zip_name in self.start_urls:
            path = "file://" + str(Path(zip_name).absolute())
            yield Request(url=path, callback=self.parse, meta={"name": zip_name})

    def parse(self, response):
        name = response.request.meta["name"]
        new_folder = name.replace(".zip", "")
        zf = ZipFile(name, 'r')
        zf.extractall(new_folder)
        zf.close()

        yield {
            "folder_name": new_folder
        }
