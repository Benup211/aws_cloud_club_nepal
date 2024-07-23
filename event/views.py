from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import EventSystem
# Create your views here.
class EventDetail(View):
    def get(self,request,id):
        event=get_object_or_404(EventSystem,id=id)
        return render(request,'event/eventDesc.html',{'event':event})
    
class EventList(View):
    def get(self,request):
        events=EventSystem.objects.all()
        return render(request,'event/eventlist.html',{'events':events})