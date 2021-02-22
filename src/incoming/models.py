from django.db import models

from profiles.models import Event, Person


class EventProposal(models.Model):
    real_event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name="real_event",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=256)
    detail = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class RelationProposal(models.Model):
    event = models.ForeignKey(EventProposal, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    date = models.DateField()
