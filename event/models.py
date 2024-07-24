from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from AWSUser.models import User
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
    detail=CKEditor5Field('Text',config_name='extends')
    EventStatus = models.CharField(max_length=20, choices=[
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ], help_text="Select the current status of the event.")

    class Meta:
        verbose_name="AWS Event"
        verbose_name_plural="AWS Events"
    def __str__(self):
        return self.title

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
    detail=CKEditor5Field('Text',config_name='extends')
    EventStatus = models.CharField(max_length=20, choices=[
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ], help_text="Select the current status of the event.")

    class Meta:
        verbose_name="AWS Grand Event"
        verbose_name_plural="AWS Grand Events"
    def __str__(self):
        return self.title

class GuestSpeaker(models.Model):
    SpeakerName = models.CharField(max_length=100)
    SpeakerTitle = models.CharField(max_length=100)
    SpeakerBio = models.TextField()
    SpeakerPhoto = models.ImageField(upload_to='speaker_photos', null=True, blank=True)
    class Meta:
        verbose_name="AWS Guest Speaker"
        verbose_name_plural="AWS Guest Speakers"
    def __str__(self):
        return f"{self.SpeakerName} {self.SpeakerTitle}"

class EventParticipant(models.Model):
    account_suscriber=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    event_suscribed=models.ForeignKey(EventSystem,on_delete=models.CASCADE,blank=False,null=False)
    participant_suscriber=models.EmailField(blank=True,null=True)
    class Meta:
        unique_together = [
            ('event_suscribed', 'account_suscriber'),
            ('event_suscribed', 'participant_suscriber'),
        ]

    def __str__(self):
        return f"{self.event_suscribed} participated by {self.account_suscriber} {self.participant_suscriber}"