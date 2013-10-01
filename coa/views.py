from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404 
from django.core.urlresolvers import reverse
from django.template import RequestContext
from coa.models import Account, AccountForm
from journal.models import FieldSet 

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def account_edit(request, account_id=None):

    account = None
    if account_id is not None:
        account = Account.objects.get(pk=account_id)

    if request.POST:
        form = AccountForm(data=request.POST, instance=account)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/coa')
        else:
            messages.error(request, 'Wrong data, check it out!')
    else:
        form = AccountForm(instance=account)

    fieldsets = (FieldSet(form, ('accno','description'),
                        legend='',
                        cls=""),
                FieldSet(form, ('chart_type','category'), 
                        legend='') )

    return render_to_response('coa/account_edit.html', RequestContext(request, {'form' : form, 'fieldsets' : fieldsets}))

