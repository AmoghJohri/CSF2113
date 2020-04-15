# CSF2113

This project scrapes information from a website and then formats the output into a csv file. 

It uses the following website as an example:

https://www.amazon.in/s?k=earphones+with+mic&i=electronics&rh=p_72%3A1318476031&dc&crid=2N58U5A6XCGT2&qid=1586958396&rnid=1318475031&sprefix=ear%2Celectronics%2C355&ref=sr_nr_p_72_1

The website contains information about the latest earphones with ratings above 4 stars.

The ScraperProject contains the code to scrape product name, image links and ratings of the various earphones displayed.

Instructions to run the Scraper:

1. Go to the WebsiteScraper folder in the ScraperProject folder.
2. Run the command - scrapy crawl website_spider -o items.json
This command will create an output file named items.json in your directory which will contain the extracted information. 
Please Note: You need to remove the items.json file each time before rerunning the code.

This data in the json file is then given as an input to the formatter to be converted into a csv file.
