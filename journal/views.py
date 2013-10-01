# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404 
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.forms.models import inlineformset_factory
from journal.models import Trans, TransForm, Item, ItemForm, FieldSet

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def entry_edit(request, trans_id=None):

    if  trans_id == None:
        trans = Trans()
    else:
        trans = Trans.objects.get(id = trans_id)

    ItemFormSet  = inlineformset_factory(Trans, Item, form=ItemForm, extra=4)    
    
    if request.method == "POST":
        transform      = TransForm(request.POST, instance=trans)
        itemformset    = ItemFormSet(request.POST, request.FILES, instance=trans)
        
        if transform.is_valid() and itemformset.is_valid():
            transform.save()
            itemformset.save()

            # Redirect to somewhere
            #if '_save' in request.POST:
            return HttpResponseRedirect('/journal')

        else:
            messages.error(request, 'Wrong data, check it out!')
                
    else:
        transform      = TransForm(instance=trans)
        itemformset    = ItemFormSet(instance=trans)

    fieldsets = (FieldSet(transform, ('reference','description'),
                        legend='',
                        cls=''),
                #FieldSet(transform, ('doctype','project','trans_date'), 
                FieldSet(transform, ('doctype','trans_date'), 
                        legend='') )

    return render_to_response('journal/entry_edit.html', RequestContext(request, {
        'transform'    : transform,
        'fieldsets'    : fieldsets,
        'itemformset'  : itemformset,
    })) 
