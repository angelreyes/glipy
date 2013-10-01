from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

@login_required 
def myinfo( request, template_name = 'accounts/settings.html' ):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    page_title = 'Account Settings'
    if request.method == 'POST':
#        postdata = request.POST.copy()
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserChangeForm(instance=request.user)
    title = 'Settings'
    return render_to_response( template_name, locals(), context_instance = RequestContext( request) )
