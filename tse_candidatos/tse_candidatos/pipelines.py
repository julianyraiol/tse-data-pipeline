# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os
import scrapy
from scrapy.pipelines.files import FilesPipeline

from urllib.parse import urlparse
from itemadapter import ItemAdapter


# class TseCandidatosPipeline:
#     def process_item(self, item, spider):
#         return item


class TseCandidatosDownloadPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        adapter = ItemAdapter(item)
        for file_url in adapter['file_urls']:
            yield scrapy.Request(file_url)
