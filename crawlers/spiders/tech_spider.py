from django.db import IntegrityError
from scrapy import Spider
from scrapy.selector import Selector

from ..items import TechnologyDjangoItem


class TechSpider(Spider):
    name = "tech"
    allowed_domains = ["technewsworld.com"]
    start_urls = [
        "http://www.technewsworld.com/",
    ]

    def parse(self, response):
        news_list = Selector(response).xpath(
            '//div[@class="story-list xlarge shadow-big"]'
        )

        for news_item in news_list:
            try:
                title = news_item.xpath(
                    'div[@class="title"]/a/text()'
                ).extract()[0]
                description = news_item.xpath(
                    'div[@class="teaser"]/text()').extract()[0]
                url = 'http://www.technewsworld.com' + news.xpath(
                    'div[@class="title"]/a/@href').extract()[0]
                image_url = 'http://www.technewsworld.com' + news.xpath(
                    'div[@class="image"]/a/img/@src').extract()[0]
            except IndexError:
                continue

            item = TechnologyDjangoItem(
                title=title,
                description=description,
                url=url,
                image_url=image_url
            )
            # DjangoItem objects lack convenience methods of model objects like
            # update_or_create. So a quick and dirty error handling is done here
            try:
                item.save()
            except IntegrityError:
                continue

            yield item
