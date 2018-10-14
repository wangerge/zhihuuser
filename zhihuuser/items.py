# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field

class UserItem(Item):
    # define the fields for your item here like:
    id = Field()
    name = Field()
    answer_count = Field()
    articles_count = Field()
    follower_count = Field()
    gender = Field()
    headline = Field()
    type = Field()
    url_token = Field()
    employments = Field()
    avatar_url_template = Field()
    avatar_url = Field()





