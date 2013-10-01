from django.db import models
from django.forms import ModelForm, TextInput, Select
from coa.models import Account

TAX_CALC_TYPE_CHOICES = (
    ('P','Percentage'),
    ('F','Fixed Value'),
)

# Create your models here.
class Tax(models.Model):
    taxno = models.CharField(max_length=16, null=False)
    description = models.CharField(max_length=256, null=False)
    account = models.ForeignKey(Account)
    calc_type = models.CharField(max_length=1, choices=TAX_CALC_TYPE_CHOICES, null=False, default='P')
    percentage = models.DecimalField(max_digits=7, decimal_places=5) 
    fixed_value = models.DecimalField(max_digits=14, decimal_places=5) 

    def __unicode__(self):
        return self.description

class TaxForm(ModelForm):
    class Meta:
        model = Tax
        widgets = {
            'taxno': TextInput(attrs={'placeholder': 'Tax ID', 'size':'50', 'class':'span5'}),
            'description': TextInput(attrs={'placeholder': 'description', 'size':'70', 'class':'span5'}),
            'account': Select(attrs={'class':'small'}),
            'calc_type': Select(attrs={'class':'small'}),
            'percentage': TextInput(attrs={'placeholder': 'Percentage', 'size':'70', 'class':'span5'}),
            'fixed_value': TextInput(attrs={'placeholder': 'Value', 'size':'70', 'class':'span5'}),
        }
