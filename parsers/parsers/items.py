# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class ParsersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HasjobItem(Item):
	title = Field()
	city = Field()
	date = Field()
	company_id = Field()
	url = Field()

	# to take from next page
	posted_date = Field()
	posted_by = Field()
	company_url = Field()
	company_image_url = Field()
	description = Field()
	type_id = Field() # Fulltime, Parttime etc.
	category_id = Field() # Programming etc.



