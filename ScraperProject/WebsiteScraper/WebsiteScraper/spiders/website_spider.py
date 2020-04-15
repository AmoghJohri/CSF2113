import scrapy
import csv
from ..items import WebsitescraperItem

class WebsiteSpiderSpider(scrapy.Spider):
    name = 'website_spider'
    start_urls = ['https://www.amazon.in/s?k=earphones+with+mic&i=electronics&rh=p_72%3A1318476031&dc&crid=2N58U5A6XCGT2&qid=1586958396&rnid=1318475031&sprefix=ear%2Celectronics%2C355&ref=sr_nr_p_72_1']

    def parse(self, response):
            product = WebsitescraperItem()

            product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
            product_image_link = response.css('.s-image-fixed-height .s-image::attr(src)').extract()
            product_rating = response.css('.a-icon-alt::text').extract()
            # product_price = response.css('.a-price-whole::text').extract()

            product['product_name'] =  product_name
            product['product_image_link'] =  product_image_link
            product['product_rating'] = product_rating[4:]
            # product['product_price'] =  product_price

            yield product

    pass
