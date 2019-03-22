import scrapy

# Reference: https://python.gotrained.com/scrapy-tutorial-web-scraping-craigslist/

class ImmobiliareSpider(scrapy.Spider):
    name = "immobiliare"

    # Mapping html elements using Xpath

    #'Next Page' button mapping
    NEXT_PAGE = '//ul[contains(@class, \'pull-right\') and contains(@class ,\'pagination\')]//li[1]//a/@href'

    # Mpping basic AD item informations
    ADS_ITEMS = '//div//ul[@class="annunci-list"]//li//div[@class="listing-item_body"]'
    ADS_ITEM_TITLE = './/p/a//@title'
    ADS_ITEM_URL = './/p/a//@href'

    # MApping the description corresponding to a specific AD
    ADS_DESCRIPTION = '//div[contains(@class ,"text-compressed")]//div/text()'

    PAGE_COUNT = 1

    start_urls = ["https://www.immobiliare.it/vendita-case/roma/"]

    # def start_requests(self):
    #     urls = ["https://www.immobiliare.it/vendita-case/roma/"]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for ads in response.xpath(self.ADS_ITEMS):
            meta = {
                "page": self.PAGE_COUNT,
                "ads_title": ads.xpath(self.ADS_ITEM_TITLE).extract_first(),
                "ads_url":   ads.xpath(self.ADS_ITEM_URL).extract_first()
            }
            yield scrapy.Request(url=meta["ads_url"], callback=self.parse_ads_details, meta=meta)

        next_page = response.xpath(self.NEXT_PAGE).extract_first()

        # crawls only the first 5 pages
        if next_page is not None and self.PAGE_COUNT < 5:
            self.PAGE_COUNT += 1
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_ads_details(self, response):
        description = "".join(line for line in response.xpath(self.ADS_DESCRIPTION).extract())
        yield {
                "page": response.meta["page"],
                "ads_title": response.meta["ads_title"],
                "ads_url": response.meta["ads_url"],
                "ads_descr": description
        }
