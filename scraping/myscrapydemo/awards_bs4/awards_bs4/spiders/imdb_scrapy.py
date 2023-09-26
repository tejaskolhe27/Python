import scrapy

class awards_bs4(scrapy.Spider):
    name = 'awards_bs4'
    start_urls = ['https://www.imdb.com/search/title/?release_date=2022-01-01,2023-12-31']

    def parse(self, response):
        movie_containers = response.css('div.lister-item.mode-advanced')

        for movie in movie_containers:
            name = movie.css('h3 a::text').get()
            rating = movie.css('strong::text').get(default="Null")
            year = movie.css('span.lister-item-year.text-muted.unbold::text').get()

            yield {
                'NAME': name,
                'RATINGS': rating,
                'YEAR': year,
            }
