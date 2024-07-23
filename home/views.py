from django.shortcuts import render
from django.views import View
from event.models import GrandEventSystem,EventSystem
from blog.models import AWSBlog
class HomeView(View):

    def get(self,request):
        latest_events = EventSystem.objects.order_by('-startDate')[:3]
        latest_blogs=AWSBlog.objects.order_by('-date_of_publish')[:3]
        context={
            'events':latest_events,
            'blogs':latest_blogs
        }
        return render(request,'home/homepage.html',context)