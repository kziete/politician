import datetime

import pytest

from incoming.models import EventProposal
from incoming.usecases.acceptevent import AcceptEvent
from incoming.usecases.collector import CollectNews
from incoming.usecases.crawlers import Page
from profiles.models import Event, Person


@pytest.fixture
def new_event_proposal() -> EventProposal:
    return EventProposal(
        title="New Event", detail="Detail", date=datetime.datetime.now().date()
    )


class MockEventRepository:
    def create_event(self, new_event):
        return new_event

    def update_event_proposal(self, proposal):
        pass


class TestAcceptEvent:
    def test_create(self, new_event_proposal):
        repo = MockEventRepository()
        usecase = AcceptEvent(repo).set_params(new_event_proposal)

        event = usecase.execute()

        assert type(event) == Event
        assert event.title == new_event_proposal.title
        assert event.detail == new_event_proposal.detail
        assert event.date == new_event_proposal.date


class MockCollectRepository:
    def get_people(self):
        return [
            Person(first_name="Sebastián", last_name="Piñera"),
            Person(first_name="Michelle", last_name="Bachelet"),
        ]


class MockCrawler:
    def execute(self):
        return [
            Page("", "titulo", "detail"),
            Page("http://google.com", "sebastián piñera", "es muy malo"),
        ]


class TestCollectNews:
    def test_collect(self):
        usecase = CollectNews(MockCollectRepository())
        usecase.add_crawler(MockCrawler())
        usecase.execute()
