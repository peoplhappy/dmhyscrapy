# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmhyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field() #h3
    urls=scrapy.Field(); # url连接
    # #tabs-1 > p:nth-child(1) > a 会员下载连接
    # #a_magnet 磁链 1
    # #magnet2  磁链2
    # #ddplay  弹幕

    pass
