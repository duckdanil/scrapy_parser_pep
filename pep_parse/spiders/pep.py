import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.css(
            'section[id="numerical-index"]').css('a[href^="pep-"]')
        for link in links:
            pep_url = response.urljoin(link.attrib['href']) + '/'
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = (
            response.css('h1.page-title::text').get().split(' – ', 1))
        data = {
            'number': number.split()[1],
            'name': name,
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
