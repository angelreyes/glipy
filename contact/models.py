from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=256, null=False)
    taxid = models.CharField(max_length=32, null=False)
    nickname = models.CharField(max_length=64)
    address1 = models.CharField(max_length=256, null=False)
    address2 = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    phone = models.CharField(max_length=64)
    email = models.EmailField(max_length=75)
    twitter = models.CharField(max_length=64)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
       model = Contact 
       widgets = {
           'name': TextInput(attrs={ 'size':'70', 'placeholder':"Name", 'class':'span5'}),
           'taxid': TextInput(attrs={ 'size':'70', 'placeholder':"Tax Id", 'class':'span5'}),
           'nickname': TextInput(attrs={ 'size':'70', 'placeholder':'Nickname', 'class':'span5'}),
           'address1': TextInput(attrs={ 'size':'70', 'placeholder':"Address 1", 'class':'span5'}),
           'address2': TextInput(attrs={ 'size':'70', 'placeholder':"Address 2", 'class':'span5'}),
           'state': TextInput(attrs={ 'size':'70', 'placeholder':"State", 'class':'span5'}),
           'country': TextInput(attrs={ 'size':'70', 'placeholder':"Country", 'class':'span5'}),
           'phone': TextInput(attrs={ 'size':'70', 'placeholder':"Phone", 'class':'span5'}),
           'email': TextInput(attrs={ 'size':'70', 'placeholder':"Email", 'class':'span5'}),
           'twitter': TextInput(attrs={ 'size':'70', 'placeholder':"Twitter", 'class':'span5'}),
           'website': TextInput(attrs={ 'size':'70', 'placeholder':"Web Site", 'class':'span5'}),
       }
