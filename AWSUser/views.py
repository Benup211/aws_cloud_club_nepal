from django.shortcuts import render
from .forms import AWSMembershipRegisterForm
from django.views import View

class MembershipRegister(View):

    def get(self,request):
        form = AWSMembershipRegisterForm()
        return render(request, 'AWSUser/User_Register.html', {'form': form})
    def post(self,request):
        form=AWSMembershipRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            return {"msg":"sucessful"}
        else:
            return render(request, 'AWSUser/User_Register.html', {'form': form})

