from django.urls import path

from . import views

urlpatterns = [
    path('',views.authorization,name="authorization"),
    path('requests/',views.user_requests,name="user_requests"),
    path('mainpage/',views.mainpage,name="mainpage"),
]