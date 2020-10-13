# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import scrapy
from scrapy.pipelines.files import FilesPipeline
from itemadapter import ItemAdapter
from elasticsearch import Elasticsearch
from functools import wraps


def check_spider_pipeline(process_item_method):
    @wraps(process_item_method)
    def wrapper(self, item, spider):
        try:
            if self.__class__ in spider.pipeline:
                return process_item_method(self, item, spider)
        except AttributeError:
            pass
        return item
    return wrapper


class TseCandidatosDownloadPipeline(FilesPipeline):
    def file_path(self, request):
        return request.meta['filename']

    def get_media_requests(self, item):
        adapter = ItemAdapter(item)
        for file_url in adapter['file_urls']:
            yield scrapy.Request(file_url, meta={"filename": adapter["filename"]})


class ElasticsearchPipeline(FilesPipeline):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    @check_spider_pipeline
    def process_item(self, item, spider):
        return item
