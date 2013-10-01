
from django.db import models
from django.forms import ModelForm, TextInput, Select, RadioSelect
import datetime


ACCOUNT_CHART_TYPE_CHOICES = (
    ('A','Account'),
    ('H','Header'),
)

ACCOUNT_CATEGORY_CHOICES = (
    ('A','Asset'),
    ('L','Liability'),
    ('Q','Equity'),
    ('I','Income'),
    ('E','Expense'),
    ('O','Off Balance-Sheet'),
)

# Create your models here.
class Account(models.Model):
    accno = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=256, null=False)
    chart_type = models.CharField(max_length=1, choices=ACCOUNT_CHART_TYPE_CHOICES, null=False, default='A')
    category = models.CharField(max_length=1, choices=ACCOUNT_CATEGORY_CHOICES, null=False, default="A")

    def __unicode__(self):
        return self.description


class AccountForm(ModelForm):
    class Meta:
        model = Account
        widgets = {
            'accno': TextInput(attrs={'placeholder': 'Account number', 'size':'50', 'class':'span5'}),
            'description': TextInput(attrs={'placeholder': 'Description', 'size':'70', 'class':'span5'}),
            'chart_type': Select(attrs={'class':'small'}),
            'category': Select(attrs={'class':'small'}),
        }
