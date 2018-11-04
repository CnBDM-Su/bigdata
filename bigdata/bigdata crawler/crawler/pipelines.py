# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.h

from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy import log

class CrawlerGewaraPipeline(object):
    def process_item(self,item,spider):
        return item

