#-*- coding: UTF-8 -*-   

import scrapy
from dbtest.items import DoubanmovieItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class DoubanSpider(CrawlSpider):
    name = "douban"     #爬虫名称
    allowed_domains = ["https://movie.douban.com/"]
    start_urls = ["https://movie.douban.com/top250"]
    url = 'http://movie.douban.com/top250'


    def parse(self, response):
        # print response.body
        item = DoubanmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMoive in Movies:
            title = eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = eachMoive.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            critical = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[1]
            quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # quote可能为空，因此需要先进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['critical'] = critical
            item['quote'] = quote
            yield item  # 提交生成csv文件
            nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
            # 第10页是最后一页，没有下一页的链接
            if nextLink:
             nextLink = nextLink[0]
             print nextLink
             yield Request(self.url + nextLink, callback=self.parse)
             # 递归将下一页的地址传给这个函数自己，在进行爬取
