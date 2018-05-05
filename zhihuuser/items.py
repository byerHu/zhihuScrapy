# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuuserItem(scrapy.Item):
    # 抓取的内容
    id = scrapy.Field()                         # 用户ID
    name = scrapy.Field()                       # 用户姓名
    answer_count = scrapy.Field()               # 回答数
    articles_count = scrapy.Field()             # 文章数
    business = scrapy.Field()                   # 所属行业
    employments = scrapy.Field()                # 职业经历
    columns_count = scrapy.Field()              # 专栏数
    description = scrapy.Field()                # 个人简介
    educations = scrapy.Field()                 # 教育经历
    follower_count = scrapy.Field()             # 被多少人关注
    gender = scrapy.Field()                     # 性别 1.男性 0.女性 -1.未知
    headline = scrapy.Field()                   # 个人标签
    hosted_live_count = scrapy.Field()          # 个人开的live数
    locations = scrapy.Field()                  # 居住地
    url_token = scrapy.Field()                  # 用户唯一标识
    user_type = scrapy.Field()                  # 用户类型
    logs_count = scrapy.Field()                 # 参与多少次公共编辑
    participated_live_count = scrapy.Field()    # 参加的live数

