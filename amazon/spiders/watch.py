# -*- coding: utf-8 -*-
import time
from urllib import parse

import scrapy
from lxml import etree
from scrapy import  Request

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WatchSpider(scrapy.Spider):
    name = 'watch'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=watch&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss']

    def parse(self, response):
        time.sleep(2)
        titles=response.xpath('//div[@class="sg-col-inner"]/div/h2//a[@class="a-link-normal a-text-normal"]/span/text()').extract()
        price =response.xpath('//div[@class="sg-col-inner"]//div[@class="a-row"]//span[@class="a-price"]/span[@class="a-offscreen"]/text()').extract()
        number =response.xpath('//span[@class="a-size-base"]/text()').extract()
        pingfen =response.xpath('//span[@class="a-icon-alt"]/text()').extract()

        url_1 = 'https://www.amazon.com'
        url_2= response.xpath('//div[@class="sg-col-inner"]/div/h2/a/@href').extract()
        herf = [parse.urljoin(url_1,item) for item in url_2]
        
        for item in zip(titles,price,pingfen,number,herf):
            yield{
                "title":item[0],

                "price":item[1],

                "pingfen":item[2],
                "number": item[3],
                "herf": item[4],
            }
        page_url_1 = 'https://www.amazon.com'
        page_url_2 =response.xpath('//div[@class="a-text-center"]/ul[@class="a-pagination"]/li[@class="a-last"]/a/@href').extract_first()

        if next!=None:
             next_url = parse.urljoin(page_url_1, page_url_2)
        
             yield Request(next_url)

