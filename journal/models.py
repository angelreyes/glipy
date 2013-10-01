from django.db import models
from django.forms import ModelForm, Select, TextInput, DateInput
from coa.models import Account
from contact.models import Contact
from tax.models import Tax
from doctype.models import Doctype
import datetime
from django.forms.forms import BoundField


class Trans(models.Model):
    doctype = models.ForeignKey(Doctype)
    reference = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=256, null=False)
    #project = models.ForeignKey(Project)
    trans_date = models.DateTimeField()

def make_custom_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%d/%m/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield

class TransForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Trans
#        widgets = {
#            'doctype': Select(attrs={'class':'span2'}),
#            'reference': TextInput(attrs={ 'size':'80', 'placeholder':'reference number', 'class':'span5'}),
#            'description': TextInput(attrs={ 'size':'100', 'placeholder':'transaction description', 'class':'span5'}),
#        }

class Item(models.Model):
    trans = models.ForeignKey(Trans, blank=True, null=True, on_delete=models.CASCADE)
    account = models.ForeignKey(Account)
    debit = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
    credit = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
    currency = models.CharField(max_length=3, null=False, default='MXN')
    contact = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.CASCADE)
    tax = models.ForeignKey(Tax, blank=True, null=True, on_delete=models.CASCADE)
    note = models.CharField(max_length=256, blank=True)

class ItemForm(ModelForm):
    class Meta:
        model = Item
        widgets = {
            'account': Select(attrs={'class':'span2'}),
            'debit': TextInput(attrs={ 'size':'50', 'placeholder':"$", 'class':'span2'}),
            'credit': TextInput(attrs={ 'size':'50', 'placeholder':"$", 'class':'span2'}),
            'currency': TextInput(attrs={ 'size':'40', 'class':'span2'}),
            'contact': Select(attrs={'class':'span2'}),
            'tax': Select(attrs={'class':'span2'}),
            'note': TextInput(attrs={ 'size':'50', 'placeholder':"note", 'class':'span2'}),
        }

class FieldSet(object):
    def __init__(self,form,fields,legend='',cls=None):
        self.form = form
        self.legend = legend
        self.fields = fields
        self.cls = cls
 
    def __iter__(self):
        for name in self.fields:
            field = self.form.fields[name]
            yield BoundField(self.form, field, name)
