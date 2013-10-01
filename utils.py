
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, View

class ProtectedListView(ListView):
    print "into ProtectedListView"
    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        print "into dispatch ListView"
        return super(ProtectedListView, self).dispatch(*args, **kwargs)

class ProtectedDetailView(DetailView):
    print "into ProtectedDetailView"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        print "into dispatch ListView"
        return super(ProtectedDetailView, self).dispatch(*args, **kwargs)

