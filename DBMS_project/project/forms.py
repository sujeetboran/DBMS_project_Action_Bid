from django import forms

class ItemForm(forms.Form):
    initialprice    = forms.IntegerField(label='initialprice')
    description     = forms.CharField(label='description',max_length=100)
    available       = forms.BooleanField(label='available')
    start_interval  = forms.DateField(label='start_interval')
    end_interval    = forms.DateField(label='end_interval')
    category        = forms.CharField(label='category')
    owner           = forms.CharField(label='owner')
    
class BidForm(forms.Form):
    item_id     = forms.CharField(label='item_id')
    user_detail = forms.CharField(label='user_detail')
    price       = forms.IntegerField(label='price')
    
class MessageForm(forms.Form):
    from_user   = forms.CharField(label='from_user')
    to_user     = forms.CharField(label='to_user')
    topic       = forms.CharField(label='topic',max_length=30)
    text        = forms.CharField(label='text',max_length=100)

class loginform(forms.Form):
    username    = forms.CharField(label='username')
    password    = forms.CharField(label='password')

class Categoryform(forms.Form):
    name        = forms.CharField(label='name')

class searchitemform(forms.Form):
    owner     = forms.CharField(label='owner')

class biditemform(forms.Form):
    item_id      = forms.CharField(label='item_id')

class seachMessageForm(forms.Form):
    to_user     = forms.CharField(label='to_user')