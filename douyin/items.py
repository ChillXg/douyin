# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyinItem(scrapy.Item):

    title = scrapy.Field()
    # 获取下一个索引链接
    userID = scrapy.Field()
    # 获取短视频url
    mp4_url = scrapy.Field()
    # 获取内容描述
