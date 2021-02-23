import time
from typing import List, Dict, Iterator
import urllib.request

import requests
from bs4 import BeautifulSoup

from . import Crawler, Page


class LaTerceraCrawler(Crawler):
    home_page: str = "https://www.latercera.com"
    allowed_subpages: List[str] = ["politica", "nacional"]

    def __init__(self) -> None:
        pass

    def execute(self) -> Iterator:
        response = requests.get(self.home_page)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.select("article .headline a")
        for link in links:
            path = link["href"]
            if path.split("/")[1] not in self.allowed_subpages:
                continue

            yield self.crawl_detail(path)

    def crawl_detail(self, path: str) -> Dict[str, str]:
        url = f"{self.home_page}{path}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.select("h1 > div")[0]
        paragraphs = soup.select(".paragraph")
        detail = "\n".join(map(lambda x: x.text, paragraphs))
        return Page(url, title.text, detail)


if __name__ == "__main__":
    usecase = LaTerceraCrawler()
    try:
        for page in usecase.execute():
            print(page)
    except KeyboardInterrupt:
        print("Crawl cancelado")
