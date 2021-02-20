from django.contrib import admin

from .models import Person, Event, EventRelation


admin.site.register(Person)
admin.site.register(Event)
admin.site.register(EventRelation)
