# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class BookItem(Item):
    # define the fields for your item here like:
    title = Field()
    type = Field()
    author = Field()
    img = Field()
    link = Field()

class BookType(Item):
    type = Field()
    link = Field()
