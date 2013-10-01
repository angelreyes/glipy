# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404 
from django.core.urlresolvers import reverse
from django.template import RequestContext
from contact.models import Contact, ContactForm
from journal.models import FieldSet
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def contact_edit(request, contact_id=None):

    contact = None
    if contact_id is not None:
        contact = Contact.objects.get(pk=contact_id)

    if request.POST:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact')
        else:
            messages.error(request, 'Wrong data, check it out!')
    else:
        form = ContactForm(instance=contact)

    fieldsets = (FieldSet(form, ('name','taxid','nickname','email','twitter','website' ),
                        legend='',
                        cls=""),
                FieldSet(form, ('address1','address2','state','country','phone'), 
                        legend='') )

    return render_to_response('contact/contact_edit.html', RequestContext(request, {'form' : form, 'fieldsets': fieldsets }))

