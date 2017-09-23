# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from bangumi.items import BangumiItem
from bs4 import BeautifulSoup
import pandas as pd

class Bangumi(Spider):
    
    name = 'Bangumi'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }


    def start_requests(self):
        url = 'http://bangumi.tv/anime/browser?sort=rank'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        file_object = open('thefile.txt', 'w')

        item = BangumiItem()
        alll = response.xpath('//ul[@class="browserFull"]/li')
	print(alll)
        for al in alll:
            item['ranking'] = al.xpath(
                './/div/span/text()').extract()[0]
            item['name'] = al.xpath(
                './/div/h3/a/text()').extract()[0]
            item['score'] = al.xpath(
                './/div/p[@class="rateInfo"]/small/text()'
            ).extract()[0]
            item['data'] = al.xpath(
                './/div/p[1]/text()').extract()[0]
            item['num'] = al.xpath(
                './/div/p[2]/span[2]/text()').extract()[0]
                
            yield item
     
        next_url = response.xpath('//strong[@class="p_cur"]/text()').extract()[0]
        next_url = int(next_url)+1
        print next_url
        if next_url<=170:
            next_url = 'http://bangumi.tv/anime/browser' + '?sort=rank&page=%d'%next_url
            yield Request(next_url, headers=self.headers)
