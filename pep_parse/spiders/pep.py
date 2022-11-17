from re import search

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.xpath('//section[@id="numerical-index"]')
        pep_links = peps.css(
            'a[class="pep reference internal"]::attr(href)').getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1[class=page-title]::text').get().split()
        number = title[1]
        name = title[3:]
        status = response.css('dt:contains("Status") + dd::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
