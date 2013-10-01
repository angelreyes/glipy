# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from doctype.models import Doctype, DoctypeForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def doctype_edit(request, doctype_id=None):

    doctype = None
    if doctype_id is not None:
        doctype = Doctype.objects.get(pk=doctype_id)

    if request.POST:
        form = DoctypeForm(data=request.POST, instance=doctype)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/doctype')
        else:
            messages.error(request, 'Wrong data, check it out!')
    else:
        form = DoctypeForm(instance=doctype)

    return render_to_response('doctype/doctype_edit.html', RequestContext(request, {'form' : form}))

