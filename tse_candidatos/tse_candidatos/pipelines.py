# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import scrapy
from scrapy.pipelines.files import FilesPipeline
from itemadapter import ItemAdapter


class TseCandidatosDownloadPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return request.meta['filename']

    def get_media_requests(self, item, info):
        adapter = ItemAdapter(item)
        for file_url in adapter['file_urls']:
            yield scrapy.Request(file_url, meta={"filename": adapter["filename"]})
