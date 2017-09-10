# -*- coding: utf-8 -*-
import scrapy


class FiancecrawlSpider(scrapy.Spider):
    name = 'fianceCrawl'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/stock/sl/#concept_1']

    def parse(self, response):
        pass
