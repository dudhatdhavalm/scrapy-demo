import scrapy


class MultiQuotesSpider(scrapy.Spider):
    name = 'multi_quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            item = {
                "Text": quote.css("span.text::text").extract_first(),
                "Auther": quote.css("small.author::text").extract_first(),
                "Tag": quote.css("a.tag::text").extract()
            }
            yield item
