from django.db import models
from django.forms import ModelForm


# Create your models here.
class Doctype(models.Model):
    description = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return self.description

class DoctypeForm(ModelForm):
    class Meta:
        model = Doctype
