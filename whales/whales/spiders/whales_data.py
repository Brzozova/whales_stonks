import scrapy


class WhalesDataSpider(scrapy.Spider):
    name = 'whales_data'
    allowed_domains = ['bitinfocharts.com']
    start_urls = ['https://bitinfocharts.com/pl/bitcoin/address/1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ/']

    def parse(self, response):
          print("procesing:"+response.url)
          shop_price=response.css('.trb').extract_first()
          print("Today shopping: "+shop_price)
