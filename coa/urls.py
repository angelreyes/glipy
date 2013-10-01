from django.conf.urls.defaults import * 
from django.views.generic import DetailView, ListView
from coa.models import Account
from utils import *

urlpatterns = patterns('',
    (r'^$',
        ProtectedListView.as_view(
            queryset=Account.objects.order_by('category', 'accno'),
            context_object_name='accounts_list',
            template_name='coa/index.html')),
    (r'^accounts/$', 'coa.views.account_edit'),
    (r'^accounts/(?P<account_id>\d+)/$', 'coa.views.account_edit'),
    url(r'^(?P<pk>\d+)/delete/$',
        ProtectedDetailView.as_view(
            model=Account,
            template_name='results.html'),
        name='poll_results'),
#    (r'^(?P<poll_id>\d+)/vote/$', 'coa.views.vote'),
)
