from django.db import models

class EventSystem(models.Model):
    title=models.TextField(help_text="Event title")
    description=models.TextField(help_text="Event Description")
    venue=models.TextField(help_text="Event venue")
    collaboration_with=models.TextField(help_text="Collaborated by")
    guest_speaker=models.TextField()
    image=models.ImageField(upload_to='events_poster',help_text="Event poster")
    startDate=models.DateTimeField(help_text="Event start time")
    endDate=models.DateTimeField(help_text="Event end time")
    facilitator=models.TextField(help_text="Event facilitator")
    EventStatus = models.CharField(max_length=20, choices=[
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ], help_text="Select the current status of the event.")

    class Meta:
        verbose_name="AWS Event"
        verbose_name_plural="AWS Events"

class GrandEventSystem(models.Model):
    title=models.TextField(help_text="Event title")
    description=models.TextField(help_text="Event Description")
    venue=models.TextField(help_text="Event venue")
    collaboration_with=models.TextField(help_text="Collaborated by")
    guest_speakers = models.ManyToManyField('GuestSpeaker', related_name='events',help_text="Guest speaker for the event")
    image=models.ImageField(upload_to='events_poster',help_text="Event poster")
    startDate=models.DateTimeField(help_text="Event start time")
    endDate=models.DateTimeField(help_text="Event end time")
    facilitator=models.TextField(help_text="Event facilitator")
    EventStatus = models.CharField(max_length=20, choices=[
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ], help_text="Select the current status of the event.")

    class Meta:
        verbose_name="AWS Grand Event"
        verbose_name_plural="AWS Grand Events"

class GuestSpeaker(models.Model):
    SpeakerName = models.CharField(max_length=100)
    SpeakerTitle = models.CharField(max_length=100)
    SpeakerBio = models.TextField()
    SpeakerPhoto = models.ImageField(upload_to='speaker_photos', null=True, blank=True)
    class Meta:
        verbose_name="AWS Guest Speaker"
        verbose_name_plural="AWS Guest Speakers"