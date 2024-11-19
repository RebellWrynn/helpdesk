from django.urls import path

from . import views

urlpatterns = [
    path('',views.authorization,name="authorization"),
    path('',views.user_requests,name="requests")
]