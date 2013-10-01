from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404 
from django.core.urlresolvers import reverse
from django.template import RequestContext

from tax.models import Tax, TaxForm
from journal.models import FieldSet 

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def tax_edit(request, tax_id=None):

    tax = None
    if tax_id is not None:
        tax = Tax.objects.get(pk=tax_id)

    if request.POST:
        form = TaxForm(data=request.POST, instance=tax)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tax')
        else:
            messages.error(request, 'Wrong data, check it out!')
    else:
        form = TaxForm(instance=tax)

    fieldsets = (FieldSet(form, ('taxno','description', 'account'),
                        legend='',
                        cls=""),
                FieldSet(form, ('calc_type','percentage', 'fixed_value'), 
                        legend='') )

    return render_to_response('tax/tax_edit.html', RequestContext(request, {'form' : form, 'fieldsets': fieldsets }))

