from ..items import ShoeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin


class TigerCrawlSpider(CrawlSpider):
    name = "tiger_crawl_spider"
    allowed_domains = ['zappos.com']
    start_urls = ['https://www.zappos.com/b/onitsuka-tiger-by-asics/brand/421']

    rules = (
        Rule(LinkExtractor(restrict_css=('a.gae-click\*Brand-Landing-Page-Onitsuka-Tiger-by-Asics\*Category-Navigation\*Mens-Shoes')), callback='parse_item'),
    )

    def parse_item(self, response):
        items = []

        for resp in response.xpath('.//div[@class="searchPage"]').css('article._1h6Kf'):
            item = ShoeItem()
            item['brand'] = resp.xpath('.//a/div[@class="_2jktc"]/p[@class="_1HOLv"]/span/text()').extract_first()
            item['name'] = resp.xpath('.//a/div[@class="_2jktc"]/p[@class="_3BAWv"]/text()').extract_first()
            item['price'] = resp.xpath('.//a/div[@class="_2jktc"]/p[@class="_1J1ab"]/span/text()').extract_first()
            product_link = resp.xpath('.//a/@href').extract_first()
            # join with base url
            item['product_link'] = urljoin(response.url, product_link)

            items.append(item)

        # sort items by price
        items.sort(key=lambda x: float(x['price'][1:]))

        return items







