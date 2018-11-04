# -*- coding: UTF-8 -*-
'''
This spider extracts specific content from given movie links which can be 
accessed from Redis Database by redis_key "movie_links" and stores the data
to HBase.
Moreover, this spider should export link to more reviews to Redis Database
as redis_key "more_reviews".
'''

import os
import sys
import scrapy
from scrapy_redis.spiders import RedisSpider
from crawler_gewara.items import CrawlerGewaraItem

reload(sys)
sys.setdefaultencoding('utf-8')

class MovieContentSpider(RedisSpider):
    name = "movieContent"
    redis_key = "movie_links"

    def parse(self, response):
        host = self.settings['REDIS_HOST']
        item = CrawlerGewaraItem()
        title = response.xpath('//div[@class="meta"]/div[1]/text()').extract()


        item['Title'] = title

        yield item
