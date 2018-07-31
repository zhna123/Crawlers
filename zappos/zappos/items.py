# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoeItem(scrapy.Item):

    brand = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    product_link = scrapy.Field()
