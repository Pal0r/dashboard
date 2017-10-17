from time import gmtime, strftime

from scrapy import Spider
from scrapy.selector import Selector

from ..items import ScienceDjangoItem


class ScienceSpider(Spider):
    name = "science"
    allowed_domains = ["sci-news.com"]
    start_urls = [
        "http://www.sci-news.com/",
    ]

    def parse(self, response):
        news_list = Selector(response).xpath('//div[@class="overview"]/ul[@class="list-news"]/li')

        for news in news_list:
            try:
                title = news.xpath('div[@class="news"]/a/text()').extract()[0]
                url = news.xpath('div[@class="news"]/a/@href').extract()[0]
            except IndexError:
                continue

            item = ScienceDjangoItem(title=title, url=url)
            item.save()

            yield item
