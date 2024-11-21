from django.urls import path

from . import views

urlpatterns = [
    path('authorization/',views.authorization,name="authorization"),
    path('requests/',views.user_requests,name="user_requests"),
    path('',views.mainpage,name="mainpage"),
]