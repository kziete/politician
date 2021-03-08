from __future__ import annotations
from typing import List, Iterator

from .crawlers import Crawler, Page
from profiles.models import Person


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
                self.create_proposal(person, page)

    def create_proposal(self, person: Person, page: Page):
        event_proposal = self.repository.get_or_create_event_proposal(page)

    def is_person_in_page(self, person: Person, page: Page) -> bool:
        return (
            person.lower_name in page.lower_title
            or person.lower_name in page.lower_detail
        )

    @property
    def pages(self) -> Iterator:
        for crawler in self.crawlers:
            yield from crawler.execute()
