from __future__ import annotations
from typing import List

from crawlers import Crawler


class CollectNews:
    def __init__(self, repository):
        self.crawlers: List[Crawler] = []
        self.respository = repository

    def add_crawler(self, crawler: Crawler) -> CollectNews:
        self.crawlers.append(crawler)
        return self

    def execute(self) -> None:
        for crawler in self.crawlers:
            for page in crawler.execute():
                print(page)


class MockRepository:
    pass


if __name__ == "__main__":
    from crawlers.latercera import LaTerceraCrawler

    try:
        CollectNews(MockRepository()).add_crawler(LaTerceraCrawler()).execute()
    except KeyboardInterrupt:
        print("Collect cancelado")
