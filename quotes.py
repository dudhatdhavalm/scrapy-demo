import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        self.log("I Just Visited " + response.url)

        yield {
            "Auther": response.css("small.author::text").extract_first(),
            "Text": response.css("span.text::text").extract_first(),
            "Tag": response.css("a.tag::text").extract_first()
        }
        # self.log(response.css("small.author::text").extract_first())
        # self.log(response.css("span.text::text").extract_first())
        # self.log(response.css("a.tag::text").extract_first())
