# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import RequestContext
from journal.models import Item
from coa.models import Account
from django.db.models import Sum
from decimal import *

from django.contrib.auth import logout

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def dashboard(request):
		income = Item.objects.filter(account__category="I").aggregate(Sum('debit'), Sum('credit'))
		expenses = Item.objects.filter(account__category="E").aggregate(Sum('debit'), Sum('credit'))
		income_d = Decimal(income['credit__sum'] or 0) - Decimal(income['debit__sum'] or 0)
		expenses_d = Decimal(expenses['debit__sum'] or 0) - Decimal(expenses['credit__sum'] or 0)
		return render_to_response('dashboard/dashboard.html', RequestContext(request, {'income':income_d,'expenses':expenses_d})) 

def logout_view(request):
    """docstring for fname"""
    logout(request)
    return HttpResponseRedirect('/login')
