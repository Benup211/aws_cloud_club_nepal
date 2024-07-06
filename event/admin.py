from django.contrib import admin
from .models import EventSystem,GrandEventSystem,GuestSpeaker
from unfold.admin import ModelAdmin

@admin.register(EventSystem)
class AdminEventSytem(ModelAdmin):
    list_display = ('title', 'startDate', 'endDate','EventStatus')
    list_filter = ('EventStatus',)

@admin.register(GrandEventSystem)
class AdminGrandEventSytem(ModelAdmin):
    list_display = ('title', 'startDate', 'endDate','EventStatus')
    list_filter = ('EventStatus',)

@admin.register(GuestSpeaker)
class AdminGuestSpeaker(ModelAdmin):
    list_display = ('SpeakerName', 'SpeakerTitle', 'event_titles')

    def event_titles(self,obj):
        return ', '.join([event.title for event in obj.events.all()])
    event_titles.short_description = 'Event Titles'