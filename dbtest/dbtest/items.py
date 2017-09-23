# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#电影名
    movieInfo = scrapy.Field()#电影介绍
    star = scrapy.Field()#评分
    critical = scrapy.Field()#评分人数
    quote = scrapy.Field()#经典的话
