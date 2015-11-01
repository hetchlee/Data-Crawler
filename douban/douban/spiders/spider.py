# -*- coding: utf-8 -*-
#__author__ = 'lizhen'
import scrapy

class douban(scrapy.Spider):
    name = "douban"
    start_urls = ['http://movie.douban.com/top250']
    def parse(self,response):
        print response.body

