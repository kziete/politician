from __future__ import annotations
from typing import List

from crawlers import Crawler


class CollectNews:
    def __init__(self, repository):
        self.crawlers: List[Crawler] = []
        self.repository = repository

    def add_crawler(self, crawler: Crawler) -> CollectNews:
        self.crawlers.append(crawler)
        return self

    def execute(self) -> None:
        for crawler in self.crawlers:
            for page in crawler.execute():
                for person in self.repository.get_people():
                    if person in page.lower_title or person in page.lower_detail:
                        print(f"{person} encontrado en: {page.url}")


class MockRepository:
    def get_people(self):
        return ["sebastián piñera", "michelle bachelet"]


if __name__ == "__main__":
    from crawlers.latercera import LaTerceraCrawler

    try:
        CollectNews(MockRepository()).add_crawler(LaTerceraCrawler()).execute()
    except KeyboardInterrupt:
        print("Collect cancelado")
