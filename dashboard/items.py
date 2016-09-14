# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TypeOneItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    timestamp = scrapy.Field()

class TypeTwoItem(scrapy.Item):
	title = scrapy.Field()
	description = scrapy.Field()
	url = scrapy.Field()
	image = scrapy.Field()
	timestamp = scrapy.Field()		

class TypeThreeItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    timestamp = scrapy.Field()