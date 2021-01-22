from django.contrib import admin
from .models import Person, Event, Unit, Location


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('initiator', 'arrived', 'location')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('rank', 'lname', 'fname', 'branch', 'category', 'edipi', 'unit')


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit',)
