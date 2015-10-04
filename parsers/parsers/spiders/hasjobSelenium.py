# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from parsers.items import HasjobItem

from selenium import selenium

class HasjobseleniumSpider(CrawlSpider):
	name = "hasjobSelenium"
	allowed_domains = ["hasjob.co"]
	start_urls = (
		# 'http://www.hasjob.co/',
		# 'file:///opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_7/pysite/ignore/hasjob',
		'file:///opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_7/pysite/ignore/hasjob_10_2_2015',
	)

	def parse(self, response):
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



	rules = (
		Rule(SgmlLinkExtractor(allow=('\.html', )), callback='parse_page',follow=True),
	)

	def __init__(self):
		CrawlSpider.__init__(self)
		self.verificationErrors = []
		self.selenium = selenium("localhost", 4444, "*chrome", "http://www.domain.com")
		self.selenium.start()

	def __del__(self):
		self.selenium.stop()
		print self.verificationErrors
		CrawlSpider.__del__(self)

	def parse_page(self, response):
		item = Item()

		hxs = HtmlXPathSelector(response)
		#Do some XPath selection with Scrapy
		hxs.select('//div').extract()

		sel = self.selenium
		sel.open(response.url)

		#Wait for javscript to load in Selenium
		time.sleep(2.5)

		#Do some crawling of javascript created content with Selenium
		sel.get_text("//div")
		yield item





