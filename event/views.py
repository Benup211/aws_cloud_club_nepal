from django.shortcuts import render
from django.views import View
from .models import EventSystem
# Create your views here.
class EventDetail(View):
    def get(self,request,id):
        event=EventSystem.objects.get(id=id)
        return render(request,'event/eventDesc.html',{'event':event})
    
class EventList(View):
    def get(self,request):
        events=EventSystem.objects.all()
        return render(request,'event/eventlist.html',{'events':events})