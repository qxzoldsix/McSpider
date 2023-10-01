# Scrapy settings for MOOCSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MOOCSpider'

SPIDER_MODULES = ['MOOCSpider.spiders']
NEWSPIDER_MODULE = 'MOOCSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MOOCSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
    'cookie':'EDUWEBDEVICE=3e9ad83fb5824fc5a391f6d036b1b451; MOOC_PRIVACY_INFO_APPROVED=true; hb_MA-A976-948FFA05E931_source=cn.bing.com; __yadk_uid=nmYxPWb2FCMJfAKWjZUwYqutHjeKCtfL; NTESSTUDYSI=2e72caa03e43481d9aae81bc1ef6906c; WM_NI=kvfzf8oQ%2BCj3%2BZkHFAj0puXkM057TFbNjh1LnGu%2B02ZgV4kkakZMsP84ORYqaGTjfUJW9GyLifOoGHIJ%2B3iTSsul%2BLcVUztH%2FSt3sy9vYVYkhNKesjM0b9neLR81WuFiSEU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee84e46f95babf8fec53b8928ab7c15e829a8bb1c867a686b782fb7d908ca5d8cf2af0fea7c3b92aa9aaaa9be534ad8fe5a4e939e986a5a9c54baaf0c096db618ff0fbd8d74ea292a689b448ae99bbccb33a9ab99ad5ea61a3b596aef25cfcec81b3dc7ba3999c8be55f8a89f7a8fc48abba8190c6448b96e5d4ec6091adbb8daa48a18a9b9bf744ed8dbcd4f273fbaa97b7dc61ac928586f2628ff0aedaed6f908ef8d2d67f86b79da6d837e2a3; WM_TID=%2Fk5tLvo1zyVBQFEBABPFjaYme1haXkvO; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1695796568; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1695799667'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'MOOCSpider.middlewares.MoocspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'MOOCSpider.middlewares.MoocspiderDownloaderMiddleware': 350,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'MOOCSpider.pipelines.TextPipeline': 400,
    'MOOCSpider.pipelines.MongoPipeline': 500,
}
MONGO_URI='loaclhost'
MONGO_DB='MOOC'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
