import datetime

import pytest

from incoming.models import EventProposal
from incoming.usecases.acceptevent import AcceptEvent
from profiles.models import Event


@pytest.fixture
def new_event_proposal() -> EventProposal:
    return EventProposal(
        title='New Event',
        detail='Detail',
        date=datetime.datetime.now().date()
    )


class MockEventRepository:
    def create_event(self, new_event):
        return new_event

    def update_event_proposal(self, proposal):
        pass


class TestAcceptEvent:
    def test_create(self, new_event_proposal):
        repo = MockEventRepository()
        usecase = AcceptEvent(repo)\
            .set_params(new_event_proposal)

        event = usecase.execute()

        assert type(event) == Event
        assert event.title == new_event_proposal.title
        assert event.detail == new_event_proposal.detail
        assert event.date == new_event_proposal.date
