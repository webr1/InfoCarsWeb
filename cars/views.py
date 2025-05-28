from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Cars
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home_page(request):
    cars=Cars.objects.all()
    context={
        "cars":cars
    }
    return render(request,"home.html",context)



class SignUp(CreateView):
    form_class=UserCreationForm
    template_name = "sign_up.html"
    success_url = reverse_lazy('login')




class LoginCustomView(LoginView):
    template_name = "login.html"


class LogoutView_1(LogoutView):
    http_method_names = ["get"]
    template_name = "logout.html"
    success_url = reverse_lazy('login')







def about_us(request):
    return render(request,"aboutus.html")


def car_detail(request,id):
    car = get_object_or_404(Cars,id=id)
    context={
        "car":car
    }
    return render(request,"car111.html",context)
