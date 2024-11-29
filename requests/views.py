from django.contrib.auth import authenticate,login as user_login, logout as user_logout

from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate


def authorization(request):
    
    if request.method == "POST":

        login = request.POST.get(login)
        password = request.POST.get(password)

        usr=authenticate(request, username=login,password=password)
        if usr is not None:
            user_login(request,usr)
            return HttpresponseRedirect('mainpage/')
        else:
            return render(request, "authorization.html")

    
    return render(request, "authorization.html")

def user_requests(request):
    return TemplateResponse(
        request, "requests.html"
    )

def mainpage(request):
    return TemplateResponse(
        request, "mainpage.html"
    )


# Create your views here.
