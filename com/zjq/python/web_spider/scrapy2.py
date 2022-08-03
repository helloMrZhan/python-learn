# 爬取 stackoverflow 标签

# -*- coding: UTF-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

BASE_DIR = __loader__.name

class StackOverflowTagSpider(scrapy.Spider):
    # 爬虫名字
    name = "stackoverflow_tags"

    # 爬虫运行的域名
    allowed_domains = ["stackoverflow.com"]

    # 爬虫开始爬取的第1个页面
    start_urls = ['https://stackoverflow.com/tags/synonyms?page=1']

    # 爬虫配置，ITEM_PIPELINES指定每个条目的处理类
    custom_settings = {
        'ITEM_PIPELINES': {f'{BASE_DIR}.TagPipeline': 301},
        'LOG_LEVEL': 'INFO'
    }

    def __init__(self):
        self.total_pages = 45
        self.page_count = 0

    def parse(self, response):
        # 访问的页面数+1，使用CSS查询页面内的标签文本
        self.page_count += 1
        tags = response.css('.post-tag::text')
        for tag in tags:
            yield {'name': tag.get()}

        # 找到页面底部的页码，访问下一页
        # 实现访问下一页代码
        if self.page_count < self.total_pages:
            next_page_list = response.css('a.js-pagination-item::attr(href)')
            if len(next_page_list) > 0:
                next_page = next_page_list[len(next_page_list) - 1].get()
                yield response.follow(next_page, callback=self.parse, dont_filter=True)

if __name__ == "__main__":
    settings = Settings()
    process = CrawlerProcess()
    process.crawl(StackOverflowTagSpider)
    process.start()