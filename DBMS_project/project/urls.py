
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('item/', views.item),
    path('searchItem/', views.searchItem),
    path('allItem/', views.allItem),
    path('bid/', views.bid),
    path('sold/', views.sold),
    path('searchBid/', views.searchBid),
    path('sendmessage/', views.sendmessage),
    path('viewmessage/', views.viewmessage),
    path('allsold/', views.allsold)
]