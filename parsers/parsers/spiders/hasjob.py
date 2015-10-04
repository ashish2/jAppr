# -*- coding: utf-8 -*-
import scrapy

from parsers.items import HasjobItem

class HasjobSpider(scrapy.Spider):
	name = "hasjob"
	allowed_domains = ["hasjob.co"]
	start_urls = (
		# 'http://www.hasjob.co/',
		# 'file:///opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_7/pysite/ignore/hasjob',
		'file:///opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_7/pysite/ignore/hasjob_10_2_2015',
	)

	def parse(self, response):
		# pass

		li = response.xpath("//ul[@id='stickie-area']/li")
		useless = li.pop(0)
		url = "http://www.hasjob.co"
		# for i in li:
		# 	item = HasjobItem()
		# 	item['title'] = i.xpath('.//span[@class="headline"]/text()').extract()[0]
		# 	item['city'] = i.xpath(".//span[contains(concat(' ', normalize-space(@class), ' '), ' top-left ')]/text()").extract()[0]
		# 	item['date'] = i.xpath(".//span[contains(concat(' ', normalize-space(@class), ' '), ' top-right ')]/text()").extract()[0]
		# 	item['company'] = i.xpath(".//span[contains(concat(' ', normalize-space(@class), ' '), '  bottom-right ')]/text()").extract()[0]
		# 	# instead an `a` this can also be a `div` where there are multiple grouped stickies, Check
		# 	item['job_url'] = url + i.xpath("./a/@href").extract()[0]
		# 	yield item
		
		# CALL PAGE 2 HERE, FROM PAGE 2
		# first_div
		posted_date = first_div.xpath("//p[@class='post-date']/time/@datetime").extract()[0]

		fid = rr.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), 'section first')]")
		all_a = fid.xpath(".//a")
		job_type = all_a.xpath("./@href").re(r"\/type\/(.*)")[0]
		job_category = all_a.xpath("./@href").re(r"\/category\/(.*)")[0]
		company_url = all_a.xpath("./@href").re(r"(http.*)")[0]
		job_description = rr.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' jobdescription ')]").extract()[0]


















"""
For testing purposes, use this in terminal:

scrapy shell
url="file:///opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_7/pysite/ignore/hasjob"
fetch(url)
response.body

"""

