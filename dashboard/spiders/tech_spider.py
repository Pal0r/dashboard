from time import gmtime, strftime

from scrapy import Spider
from scrapy.selector import Selector

from dashboard.items import TypeTwoItem


class TechSpider(Spider):
    name = "tech"
    allowed_domains = ["technewsworld.com"]
    start_urls = [
        "http://www.technewsworld.com/",
    ]

    def parse(self, response):
        news_list = Selector(response).xpath('//div[@class="story-list xlarge shadow-big"]')

        for news in news_list:
            item = TypeTwoItem()
            item['title'] = news.xpath(
                'div[@class="title"]/a/text()').extract()[0]
            item['description'] = news.xpath(
                'div[@class="teaser"]/text()').extract()[0]
            item['url'] = 'http://www.technewsworld.com' + news.xpath(
                'div[@class="title"]/a/@href').extract()[0]
            item['image'] = 'http://www.technewsworld.com' + news.xpath(
                'div[@class="image"]/a/img/@src').extract()[0]
            item['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            yield item