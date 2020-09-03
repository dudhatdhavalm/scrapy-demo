import scrapy


class LoginFormSpider(scrapy.Spider):
    name = 'login_form'
    allowed_domains = ['toscrape.com']
    login_url = "http://quotes.toscrape.com/login"
    start_urls = [login_url]

    def parse(self, response):
        csrf_token = response.css(
            'input[name="csrf_token"]::attr(value)').extract_first()

        data = {"csrf_token": csrf_token, "username": "abc", "password": "abc"}

        yield scrapy.FormRequest(
            url=self.login_url,
            formdata=data,
            callback=self.parse_quotes,
        )

    def parse_quotes(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            item = {
                "Text": quote.css("span.text::text").extract_first(),
                "Auther": quote.css("small.author::text").extract_first(),
                "Tag": quote.css("a.tag::text").extract()
            }
            yield item