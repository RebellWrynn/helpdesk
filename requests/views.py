from django.shortcuts import render
from django.http import HttpResponse


def user_requests(request):
    return HttpResponse("hello world")
# Create your views here.
