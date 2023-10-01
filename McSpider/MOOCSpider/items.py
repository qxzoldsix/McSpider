# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    courseName=scrapy.Field()
    university = scrapy.Field()
    category = scrapy.Field()
    enrollCount = scrapy.Field()
    overview = scrapy.Field()
    objective = scrapy.Field()
    preliminaries = scrapy.Field()
