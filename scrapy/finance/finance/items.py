# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinanceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # plate_name = scrapy.Field()
    # plate_url = scrapy.Field()
    # cpt_num = scrapy.Field()
    # avg_price = scrapy.Field()
    # range_flu = scrapy.Field()
    # range_num = scrapy.Field()
    # total_volume = scrapy.Field()
    
    plate_name = scrapy.Field()
    # plate_url = scrapy.Field()
    # com_num = scrapy.Field()
    # avg_price = scrapy.Field()
    # price_range = scrapy.Field()
    # price_fluct = scrapy.Field()
