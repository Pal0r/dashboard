from time import gmtime, strftime

from scrapy import Spider
from scrapy.selector import Selector

from ..items import MusicDjangoItem


class MusicSpider(Spider):
    name = "music"
    allowed_domains = ["youredm.com"]
    start_urls = [
        "http://www.youredm.com/news/",
    ]

    def parse(self, response):
        news_list = Selector(response).xpath('//div[@id="cb-content"]/div[@id="main"]/article[@role="article"]')

        for news in news_list:
            try:
                title = news.xpath('div[@class="cb-meta clearfix"]/h2[@class="cb-post-title"]/a/text()').extract()[0]
                url = news.xpath('div[@class="cb-meta clearfix"]/h2[@class="cb-post-title"]/a/@href').extract()[0]
                description = news.xpath('div[@class="cb-meta clearfix"]/div[@class="cb-excerpt"]/text()').extract()[0]
                image_url = news.xpath('div[@class="cb-mask cb-img-fw"]/a/img/@data-src').extract()[0]
            except IndexError:
                continue

            item = MusicDjangoItem(
                title=title,
                url=url,
                image_url=image_url,
                description=description
            )
            item.save()

            yield item
