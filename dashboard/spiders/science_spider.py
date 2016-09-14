from time import gmtime, strftime

from scrapy import Spider
from scrapy.selector import Selector

from dashboard.items import TypeThreeItem


class ScienceSpider(Spider):
    name = "science"
    allowed_domains = ["sci-news.com"]
    start_urls = [
        "http://www.sci-news.com/",
    ]

    def parse(self, response):
        news_list = Selector(response).xpath('//div[@class="overview"]/ul[@class="list-news"]/li')

        for news in news_list:
            item = TypeThreeItem()
            item['title'] = news.xpath(
                'div[@class="news"]/a/text()').extract()[0]
            item['url'] = news.xpath(
                'div[@class="news"]/a/@href').extract()[0]
            item['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            yield item