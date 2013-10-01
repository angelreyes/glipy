from django.conf.urls.defaults import * 
from django.views.generic import DetailView, ListView
from doctype.models import Doctype
from utils import *

urlpatterns = patterns('',
    (r'^$',
        ProtectedListView.as_view(
            queryset=Doctype.objects.order_by('id'),
            context_object_name='types_list',
            template_name='doctype/index.html')),
    (r'^entry/$', 'doctype.views.doctype_edit'),
    (r'^entry/(?P<doctype_id>\d+)/$', 'doctype.views.doctype_edit'),
)
