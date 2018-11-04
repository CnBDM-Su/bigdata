'''
This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "movie_links"
'''

import os
import scrapy
from urlparse import urljoin

class GewaraMovieSpider(scrapy.Spider):
    start_urls = ["https://ieeexplore.ieee.org/browse/books/title//?pageNumber=1&rowsPerPage=100"]
    name = "movieLinks"

    def parse(self, response):
        host = self.settings['REDIS_HOST']
        lists = []
        initial_lists = response.xpath('//a[@class="ng-binding ng-scope"]/@href').extract()
        print(initial_lists)
        for li in initial_lists: 
            lists.append(response.urljoin(li))
        for li in lists:
            command = "redis-cli -h " + host + " lpush movie_links " + li
            os.system(command)
            '''
        try:
            url = response.urljoin(response.xpath('//a[@class="next"]/@href').extract()[0])
        except:
            return
	yield scrapy.Request(url, callback=self.parse)
        '''
