import scrapy


class MultiPageSpider(scrapy.Spider):
    name = 'multi_page'
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
        next_url = response.css("li.next > a::attr(href)").extract_first()
        
        if next_url:
            abs_next_url = response.urljoin(next_url)
            yield scrapy.Request(url=abs_next_url, callback=self.parse)
