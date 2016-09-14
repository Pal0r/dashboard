from time import gmtime, strftime

from scrapy import Spider
from scrapy.selector import Selector

from dashboard.items import TypeTwoItem


class EntertainSpider(Spider):
    name = "entertain"
    allowed_domains = ["etonline.com"]
    start_urls = [
        "http://www.etonline.com/tv/",
    ]

    def parse(self, response):
        news_list = Selector(response).xpath('//div[@class="latest-wrapper TV"]/div[@class="latest-news thumb"]')

        for news in news_list:
            item = TypeTwoItem()
            item['title'] = news.xpath(
                'div[@class="title-wrapper"]/div[@class="title"]/a/text()').extract()[0]
            item['description'] = news.xpath(
                'div[@class="title-wrapper"]/div[@class="subTitle"]/a/text()').extract()[0]
            item['url'] = news.xpath(
                'div[@class="title-wrapper"]/div[@class="title"]/a/@href').extract()[0]
            item['image'] = news.xpath(
                'div[@class="image-wrapper"]/a/picture/img/@src').extract()[0]
            item['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            yield item