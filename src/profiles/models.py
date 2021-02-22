from django.db import models
from django.utils.translation import gettext as _


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Event(models.Model):
    title = models.CharField(max_length=256)
    detail = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class EventRelation(models.Model):
    POSITIVE = "P"
    NEGATIVE = "N"
    NEUTRAL = "U"
    KIND_CHOICES = (
        (POSITIVE, _("Positive")),
        (NEGATIVE, _("Negative")),
        (NEUTRAL, _("Neutral")),
    )
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    date = models.DateField()
