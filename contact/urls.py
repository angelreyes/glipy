from django.conf.urls.defaults import * 
from django.views.generic import DetailView, ListView
from contact.models import Contact
from utils import *

urlpatterns = patterns('',
    (r'^$',
        ProtectedListView.as_view(
            queryset=Contact.objects.order_by('name'),
            context_object_name='contacts_list',
            template_name='contact/index.html')),
    (r'^entry/$', 'contact.views.contact_edit'),
    (r'^entry/(?P<contact_id>\d+)/$', 'contact.views.contact_edit'),
)
