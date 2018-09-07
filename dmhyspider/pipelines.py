# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class DmhyspiderPipeline(object):
    csv_file=None
    def process_item(self, item, spider):
        self.csv_file = csv.writer(
            open("D:/dmhylink.csv", 'a', encoding="utf-8", newline=''))
        self.csv_file.writerow((item["name"],item["urls"]))
        return item
