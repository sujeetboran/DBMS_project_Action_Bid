from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from django.core import serializers
from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect
from .forms import *
genericResponse = {
    "success": False,
    "info": {}
}

activeuser=""
def register(request):
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            print(username)
            print(password)
            user = User(username=username, password=password)
            user.save()
            return redirect('/login/')
    else:
        form = loginform()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            print(username)
            print(password)
            try:
                user = User.objects.get(username=username)
            except Exception as error:
                form = loginform()
                print('error')
                return render(request, 'login.html', {'form': form})
            if user.password ==password:
                global activeuser
                print('correct')
                activeuser=username
                return redirect('/allItem/')
            else:
                print('password')
                form = loginform()
            return render(request, 'login.html', {'form': form})
    else:
        form = loginform()
    return render(request, 'login.html', {'form': form})

def item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            initialprice    = form.cleaned_data.get("initialprice")
            description     = form.cleaned_data.get("description")
            available       = form.cleaned_data.get("available")
            start_interval  = form.cleaned_data.get("start_interval")
            end_interval  = form.cleaned_data.get("end_interval")
            category        = form.cleaned_data.get("category")
            owner           = form.cleaned_data.get("owner")
            category=Category.objects.get(name=category)
            owner=User.objects.get(username=owner)
            item = Item(initialprice=initialprice, description=description,available=available,
                start_interval=start_interval,end_interval=end_interval, category=category,owner=owner)
            item.save()
            return redirect('/allItem/')
    else:
        form = ItemForm()
    return render(request, 'item.html', {'form': form})

def searchItem(request):
    if request.method == 'POST':
        form = searchitemform(request.POST)
        if form.is_valid():
            owner    = form.cleaned_data.get("owner")
            items = Item.objects.filter(owner=owner)
            return render(request,'searchitem.html',{'items':items})
    else:
        form = searchitemform()
    return render(request, 'searchitem_owner.html', {'form': form})
        

def searchBid(request):
    if request.method == 'POST':
        form = biditemform(request.POST)
        if form.is_valid():
            item_id    = form.cleaned_data.get("item_id")
            items = Bid.objects.filter(item_id=item_id)
            return render(request,'searchbit.html',{'items':items})
    else:
        form = biditemform()
    return render(request, 'searchbit_item.html', {'form': form})


def allItem(request):
    if request.method == 'GET':    
        items = Item.objects.all()
        print(items)
        return render(request,'searchitem.html',{'items':items})

def bid(request):
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            item_id     = form.cleaned_data.get("item_id")
            user_detail = form.cleaned_data.get("user_detail")
            price       = form.cleaned_data.get("price")
            item_id=Item.objects.get(item_id=item_id)
            user_detail=User.objects.get(username=user_detail)
            bid = Bid(item_id=item_id, user_detail=user_detail,price=price)
            bid.save()
            return redirect('/allItem/')
    else:
        form = BidForm()
    return render(request, 'bid.html', {'form': form})


def sold(request):
    if request.method == 'POST':
        form = biditemform(request.POST)
        if form.is_valid():
            
            item_id     = form.cleaned_data.get("item_id")
            item        = Item.objects.get(item_id=item_id)
            global activeuser
            if item.owner.username != activeuser:
                return render(request, 'sold.html', {'form': form})
            
            items = Bid.objects.filter(item_id=item_id)
            max=0
            user_detail=0
            
            for i in items:
                if max<i.price:
                    max=i.price
                    user_detail=i.user_detail
            itemid=Item.objects.get(item_id=item_id)
            
            obj = Sold_Item(item_id=itemid,price=max,user_detail=user_detail)
            obj.save()
            
            obj = Item.objects.get(item_id=item_id)
            obj.available=False
            obj.save()
            Bid.objects.filter(item_id=item_id).delete()
            return redirect('/allItem/')
    else:
        form = biditemform()
    return render(request, 'sold.html', {'form': form})


def sendmessage(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            from_user = form.cleaned_data.get("from_user")
            global activeuser
            if from_user != activeuser:
                return render(request, 'message.html', {'form': form})
            to_user = form.cleaned_data.get("to_user")
            topic = form.cleaned_data.get("topic")
            text = form.cleaned_data.get("text")
            from_user = User.objects.get(username=from_user)
            to_user = User.objects.get(username=to_user)
            message = Message(from_user=from_user,to_user=to_user,topic=topic,text=text)
            message.save()
            return redirect('/viewmessage/')
    else:
        form = MessageForm()
    return render(request, 'message.html', {'form': form})



def viewmessage(request):
    if request.method == "POST":
        form = seachMessageForm(request.POST)
        if form.is_valid():
            global activeuser
            to_user = form.cleaned_data.get("to_user")
            activeuser = User.objects.get(username=activeuser)
            to_user = User.objects.get(username=to_user)
            items = Message.objects.filter(from_user=activeuser,to_user=to_user)
            return render(request,'displaymessage.html',{'items':items})
    else:
        form = seachMessageForm()
    return render(request, 'searchmessage.html', {'form': form})

def allsold(request):
    if request.method == 'GET':    
        items = Sold_Item.objects.all()
        return render(request,'solditems.html',{'items':items})