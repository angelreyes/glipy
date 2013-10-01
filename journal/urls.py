from django.conf.urls.defaults import * 
from django.views.generic import DetailView, ListView
from journal.models import Trans
from utils import *

urlpatterns = patterns('',
    (r'^$',
        ProtectedListView.as_view(
            queryset=Trans.objects.order_by('trans_date'),
            context_object_name='trans_list',
            template_name='journal/index.html')),
    (r'^entry/$', 'journal.views.entry_edit'),
    (r'^entry/(?P<trans_id>\d+)/$', 'journal.views.entry_edit'),
    url(r'^(?P<pk>\d+)/delete/$',
        ProtectedDetailView.as_view(
            model=Trans,
            template_name='entry_delete.html'),
        name='entry_delete'),
)
