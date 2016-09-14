from time import gmtime, strftime

from scrapy import Spider
from scrapy.selector import Selector

from dashboard.items import TypeTwoItem


class MusicSpider(Spider):
    name = "music"
    allowed_domains = ["youredm.com"]
    start_urls = [
        "http://www.youredm.com/news/",
    ]

    def parse(self, response):
        news_list = Selector(response).xpath('//div[@id="cb-content"]/div[@id="main"]/article[@role="article"]')

        for news in news_list:
            item = TypeTwoItem()
            item['title'] = news.xpath(
                'div[@class="cb-meta clearfix"]/h2[@class="cb-post-title"]/a/text()').extract()[0]
            item['description'] = news.xpath(
                'div[@class="cb-meta clearfix"]/div[@class="cb-excerpt"]/text()').extract()[0]
            item['url'] = news.xpath(
                'div[@class="cb-meta clearfix"]/h2[@class="cb-post-title"]/a/@href').extract()[0]
            item['image'] = news.xpath(
                'div[@class="cb-mask cb-img-fw"]/a/img/@data-src').extract()[0]
            item['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            yield item