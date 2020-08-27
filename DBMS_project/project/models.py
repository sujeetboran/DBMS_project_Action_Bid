from django.db import models
from uuid import uuid4

class User(models.Model):
    username        = models.CharField(primary_key=True,max_length=50,unique=True)
    password        = models.CharField(max_length=50)
    

class Message(models.Model):
    message_id  = models.UUIDField(primary_key=True, default=uuid4, null=False)
    topic       = models.CharField(max_length=30)
    text        = models.CharField(max_length=10,null=False)
    from_user   = models.CharField(max_length=100,null=False)
    to_user     = models.ForeignKey(User,on_delete=models.CASCADE, null=True)


class Category(models.Model):
    name        = models.CharField(primary_key=True,max_length=50,null=False)
    
class Item(models.Model):
    item_id         = models.UUIDField(primary_key=True, default=uuid4, null=False)
    initialprice    = models.IntegerField(null=False)
    description     = models.CharField(max_length=100,null=False)
    available       = models.BooleanField(null=False)
    start_interval  = models.DateField(null=False)
    end_interval    = models.DateField(null=False)
    category        = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    owner           = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    
    
class Open_Bidding(models.Model):
    item_id    = models.ForeignKey(Item,on_delete=models.CASCADE)
    
    
class Sold_Item(models.Model):
    item_id     = models.ForeignKey(Item,on_delete=models.SET_NULL, null=True)
    price       = models.IntegerField(null=False)
    date        = models.DateField(auto_now_add=True)
    user_detail = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    
  
class Bid(models.Model):
    bid_id      = models.UUIDField(primary_key=True, default=uuid4, null=False)
    item_id     = models.ForeignKey(Item,on_delete=models.CASCADE,null=True)
    user_detail = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    price       = models.IntegerField(null=False)