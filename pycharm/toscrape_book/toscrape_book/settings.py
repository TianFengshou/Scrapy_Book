# -*- coding: utf-8 -*-

BOT_NAME = 'toscrape_book'

SPIDER_MODULES = ['toscrape_book.spiders']
NEWSPIDER_MODULE = 'toscrape_book.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True


# Mongodb 设置
MONGODB_URL = 'mongodb://localhost:27017'
MONGODB_DB_NAME = 'scrapy_toscrape_book'


# Exporter
# 指定导出数据的字段,并指定次序(默认导出全部,顺序随机)
FEED_EXPORT_FIELDS = ['title','category','price','star_rating','upc','stock','review_num','description',]

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'toscrape_book.pipelines.DuplicatesPipeline':200,
   'toscrape_book.pipelines.StarRatingPipeline': 300,
   'toscrape_book.pipelines.MongoDBPipline': 400,
}
