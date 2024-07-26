from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.utils import timezone
from django.views import View
from .models import EventSystem,EventParticipant,GrandEventSystem
from AWSUser.models import User
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.
class EventDetail(View):
    def get(self,request,id):
        event=get_object_or_404(EventSystem,id=id)
        return render(request,'event/eventDesc.html',{'event':event})

    def post(self,request,id):
        event=get_object_or_404(EventSystem,id=id)
        if request.user.is_authenticated:
            user = get_object_or_404(User, id=request.user.id)
            try:
                event_participant = EventParticipant.objects.create(
                    account_suscriber=user, event_suscribed=event)
                event_participant.save()
                messages.success(request, "Successfully Participated in the event")
                return redirect('event:EventList')
            except IntegrityError:
                messages.error(
                    request, "You have already registered for this event.")
                return redirect('event:EventDetail', id=id)
        else:
            participant = request.POST.get('participant_email')
            try:
                event_participant = EventParticipant.objects.create(
                    participant_suscriber=participant, event_suscribed=event)
                event_participant.save()
                messages.success(request, "Successfully Participated in the event")
                return redirect('event:EventList')
            except IntegrityError:
                messages.error(
                    request, "This email address has already registered for this event.")
                return redirect('event:EventDetail', id=id)
    
class EventList(View):
    def get(self,request):
        events=EventSystem.objects.all()
        return render(request,'event/eventlist.html',{'events':events})
    
class GrandEvent(View):
    def get(self,request,id):
        current_time = timezone.now()
        grand_event_c = GrandEventSystem.objects.filter(EventStatus='Ongoing',startDate__gt=current_time).order_by('startDate')[0]
        if (grand_event_c.id==id):
            grand_event=get_object_or_404(GrandEventSystem,id=id)
        else:
            raise Http404("Error")
        return render(request,'event/grandEvent.html',{'grand_event':grand_event})