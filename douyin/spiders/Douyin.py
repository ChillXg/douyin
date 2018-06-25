# -*- coding: utf-8 -*-
import scrapy
import json
from douyin.items import DouyinItem

class DouyinSpider(scrapy.Spider):
    name = 'Douyin'
    allowed_domains = ['www.douyin.com']
    data = {
        'user_id': '57720812347',
        'count': '21',
        'max_cursor': '0',
        'aid': '1128',
        '_signature': '699y1BAYsQYA0l0d5MAnUuvfcs'
    }
    url = 'https://www.douyin.com/share/user/57720812347'
    start_urls = ['https://www.douyin.com/aweme/v1/aweme/favorite/?user_id=57720812347&min_cursor=0&count=200']




    def parse(self, response):
        result = json.loads(response.text)['aweme_list']
        for each in result:
            item = DouyinItem()
            item['title'] = each['share_info']['share_title']
            item['userID'] = each['text_extra']
            if item['userID']:
                for userID in item['userID']:
                    item['userID'] = userID['user_id']
                    print(item['userID'])
            yield item
        yield scrapy.Request(self.url, callback=self.parse2)

    def parse2(self, response):
        print('\n')
        print(response.text)
