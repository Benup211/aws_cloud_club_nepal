from django.urls import path
from .views import EventDetail
urlpatterns = [
    path('view/<int:id>',EventDetail.as_view(),name="EventDetail")
]
