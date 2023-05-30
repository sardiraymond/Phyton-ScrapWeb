from pathlib import Path

import scrapy


class kaskus(scrapy.Spider):
    name = "thelounge"

    def start_requests(self):
        urls = [
            "https://www.kaskus.co.id/komunitas/21/the-lounge?tab=threads&page=1",
            "https://www.kaskus.co.id/komunitas/21/the-lounge?tab=threads&page=2",
            "https://www.kaskus.co.id/komunitas/21/the-lounge?tab=threads&page=3",
            "https://www.kaskus.co.id/komunitas/21/the-lounge?tab=threads&page=4",
            "https://www.kaskus.co.id/komunitas/21/the-lounge?tab=threads&page=5",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = f"thelounge-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")