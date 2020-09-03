import scrapy


class DetailPageSpider(scrapy.Spider):
    name = 'detail_page'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        urls = response.css("div.quote > span > a::attr(href)").extract()

        for url in urls:
            author_url = response.urljoin(url)
            yield scrapy.Request(url=author_url, callback=self.detail_parse)
        
        next_url = response.css("li.next > a::attr(href)").extract_first()
        if next_url:
            abs_next_url = response.urljoin(next_url)  
            yield scrapy.Request(url=abs_next_url, callback=self.parse)          

    def detail_parse(self, response):
        yield {
            "author_name": response.css("h3.author-title::text").extract_first().strip(),
            "born_date": response.css("span.author-born-date::text").extract_first()
        }