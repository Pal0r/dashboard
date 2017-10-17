from time import gmtime, strftime

from scrapy import Spider
from scrapy.selector import Selector

from ..items import EntertainmentDjangoItem


class EntertainSpider(Spider):
    name = "entertain"
    allowed_domains = ["etonline.com"]
    start_urls = [
        "http://www.etonline.com/tv/",
    ]

    def parse(self, response):
        news_list = Selector(response).xpath(
            '//div[@class="latest-wrapper TV"]/div[@class="latest-news thumb"]'
        )

        for news in news_list:
            try:
                title = news.xpath(
                    'div[@class="title-wrapper"]/div[@class="title"]/a/text()'
                ).extract()[0]
                description = news.xpath(
                    'div[@class="title-wrapper"]/div[@class="subTitle"]/a/text()'
                ).extract()[0]
                url = news.xpath(
                    'div[@class="title-wrapper"]/div[@class="title"]/a/@href'
                ).extract()[0]
                image_url = news.xpath(
                    'div[@class="image-wrapper"]/a/picture/img/@src'
                ).extract()[0]
            except IndexError:
                continue

            item = EntertainmentDjangoItem(
                title=title,
                description=description,
                url=url,
                image_url=image_url
            )
            item.save()

            yield item
