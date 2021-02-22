import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class LaTerceraCrawler:
    home_page = 'https://www.latercera.com'

    def __init__(self) -> None:
        pass

    def execute(self) -> None:
        response = requests.get(self.home_page)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.select('article .headline a')
        for link in links:
            path = link['href']
            if not path.startswith('/'):
                continue

            self.crawl_detail(path)

    def crawl_detail(self, path: str):
        url = f'{self.home_page}{path}'
        print(url)
        # response = requests.get(self.home_page)


if __name__ == '__main__':
    usecase = LaTerceraCrawler()
    usecase.execute()
