from profiles.models import Event
from .models import EventProposal


class EventRepository:
    def create_event(self, event: Event):
        print("create_event")

    def update_event_proposal(self, proposal: EventProposal):
        print("update event proposal")
