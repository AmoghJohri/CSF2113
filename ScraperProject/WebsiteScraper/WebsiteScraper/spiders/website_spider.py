import scrapy
import csv
from ..items import WebsitescraperItem

class WebsiteSpiderSpider(scrapy.Spider):
    name = 'website_spider'
    start_urls = ['https://www.amazon.in/s?k=earphones+with+mic&i=electronics&crid=2N58U5A6XCGT2&sprefix=ear%2Celectronics%2C355&ref=nb_sb_ss_i_2_3']

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
