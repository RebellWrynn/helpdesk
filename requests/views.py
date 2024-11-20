from django.shortcuts import render
from django.template.response import TemplateResponse
from templates import authorization.html


def authorization(request):
    return TemplateResponse(
        request, "authorization.html"
    )

def user_requests(request):
    return TemplateResponse(
        request, "requests.html"
    )
# Create your views here.
