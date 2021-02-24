from __future__ import annotations
from typing import List, Iterator

from crawlers import Crawler, Page


class CollectNews:
    def __init__(self, repository):
        self.crawlers: List[Crawler] = []
        self.repository = repository

    def add_crawler(self, crawler: Crawler) -> CollectNews:
        self.crawlers.append(crawler)
        return self

    def execute(self) -> None:
        for page in self.pages:
            self.find_persons_in_page(page)

    def find_persons_in_page(self, page: Page) -> None:
        for person in self.repository.get_people():
            if self.is_person_in_page(person, page):
                print(f"{person} encontrado en: {page.url}")

    def is_person_in_page(self, person: str, page: Page) -> bool:
        return person in page.lower_title or person in page.lower_detail

    @property
    def pages(self) -> Iterator:
        for crawler in self.crawlers:
            yield from crawler.execute()


class MockRepository:
    def get_people(self):
        return ["sebastián piñera", "michelle bachelet"]


if __name__ == "__main__":
    from crawlers.latercera import LaTerceraCrawler

    try:
        usecase = CollectNews(MockRepository())
        usecase.add_crawler(LaTerceraCrawler())
        usecase.execute()
    except KeyboardInterrupt:
        print("Collect cancelado")
