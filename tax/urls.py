from django.conf.urls.defaults import * 
from django.views.generic import DetailView, ListView
from tax.models import Tax
from utils import *

urlpatterns = patterns('',
    (r'^$',
        ProtectedListView.as_view(
            queryset=Tax.objects.order_by('taxno'),
            context_object_name='taxes_list',
            template_name='tax/index.html')),
    (r'^entry/$', 'tax.views.tax_edit'),
    (r'^entry/(?P<tax_id>\d+)/$', 'tax.views.tax_edit'),
)
