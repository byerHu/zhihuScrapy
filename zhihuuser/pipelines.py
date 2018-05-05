#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings


class ZhihuuserPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 如果数据库的登陆需要账号密码的话
        # self.client.admin.authenticate(setting['MONGO_USER'],setting['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]   # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]   # 获得collection的句柄
    def process_item(self, item, spider):
        postItem = dict(item)   # 把item转化成字典形式
        # self.coll.insert(postItem)  #向数据库插入一条记录
        # 这里通过mongodb进行了一个去重的操作，每次更新插入数据之前都会进行查询，判断要插入的url_token是否已经存在，如果不存在再进行数据插入，否则放弃数据
        self.coll.update({'url_token': postItem["url_token"]}, {'$set': postItem}, True)
        return item   # 会在控制台输出原item数据，可以选择不写

