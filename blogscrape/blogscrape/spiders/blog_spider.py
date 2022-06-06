import scrapy


class BlogSpider(scrapy.Spider):
    name = "blog"
    
    start_urls = [
        "https://www.zyte.com/blog/",
    ]
    
    def parse(self, response):
        for item in response.css('a.oxy-post-title::text').getall():
            yield{
                "title":item
            }
            
        next_page = response.css("a.next.page-numbers::attr(href)").get()
        if next_page != None:
            next_page = response.urljoin(next_page)
            
            yield scrapy.Request(next_page, callback=self.parse)
