import scrapy

from ..items import PepParseItem
from ..utils import extract_pep_data


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Возвращает ссылки на страницы PEP."""
        pep_table = response.css('section#numerical-index tbody')
        pep_links = set(pep_table.css('a[href^="pep-"]::attr(href)').getall())
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Собирает данные со страницы PEP."""
        pep_heading = ''.join(response.xpath(
            '//section[@id="pep-content"]/h1/descendant::text()').extract())
        number, name = extract_pep_data(pep_heading)
        status = response.xpath(
            '//*[@id="pep-content"]/dl/dt[contains(., "Status")]'
            '/following-sibling::dd/abbr/text()').get()
        data = {
            'number': int(number),
            'name': name,
            'status': status
        }
        return PepParseItem(data)
