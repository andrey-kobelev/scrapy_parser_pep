import re

import scrapy

from pep_parse.items import PepParseItem


PEP_NAME_REPLACE_PATTERN = re.compile(r'^PEP\s\d*\s\W*\s')


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css(
            '#pep-content table[class="pep-zero-table '
            'docutils align-default"] '
            'a[class="pep reference internal"]'
        ):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        yield PepParseItem(
            number=response.css(
                'ul.breadcrumbs li:last-child::text'
            ).get().replace('PEP ', ''),
            name=re.sub(
                pattern=PEP_NAME_REPLACE_PATTERN,
                repl='',
                string=response.css('h1.page-title::text').get()
            ),
            status=response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get()
        )
