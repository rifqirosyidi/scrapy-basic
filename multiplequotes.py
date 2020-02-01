# -*- coding: utf-8 -*-
import scrapy


class MultiplequotesSpider(scrapy.Spider):
    name = 'multiplequotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = {
                'author': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }

            yield item
