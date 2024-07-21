from django.urls import path
from .views import MembershipRegister
app_name="AWSUser"
urlpatterns = [
    path("register/",MembershipRegister.as_view(),name="register"),
]
