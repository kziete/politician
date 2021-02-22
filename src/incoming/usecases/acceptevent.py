from ..repositories import EventRepository
from ..models import EventProposal
from profiles.models import Event


class AcceptEvent:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    def set_params(self, event_proposal: EventProposal):
        self.event_proposal = event_proposal
        return self

    def execute(self):
        if self.event_proposal.real_event:
            return self.event_proposal.real_event

        new_event = Event(
            title=self.event_proposal.title,
            detail=self.event_proposal.detail,
            date=self.event_proposal.date,
        )
        event = self.repository.create_event(new_event)
        self.event_proposal.event = event
        self.repository.update_event_proposal(self.event_proposal)

        return event
