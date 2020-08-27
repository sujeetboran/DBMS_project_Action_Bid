from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Open_Bidding)
admin.site.register(Sold_Item)
admin.site.register(Bid)