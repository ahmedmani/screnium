from scrapy import signals
from itemadapter import is_item, ItemAdapter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER as log12
from scrapy.http import HtmlResponse
import logging
log12.setLevel(logging.WARNING)


class ScreniumDownloaderMiddleware:


    def __init__(self):   
        self.driver = webdriver.Chrome()

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        self.driver.get(request.url)
        return HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding="UTF-8" )
        # return None

    def process_response(self, request, response, spider):
        return response


    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
