# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']

    def parse(self, response):
        filename =  response.url.split("/")[-2]
        print filename
        with open(filename,"wb") as f:
            f.write(response.body)
