from django.conf.urls.defaults import * 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from views import myinfo
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('dashboard.urls')),
    (r'^dashboard/', include('dashboard.urls')),
    (r'^coa/', include('coa.urls')),
    (r'^journal/', include('journal.urls')),
    (r'^contact/', include('contact.urls')),
    (r'^tax/', include('tax.urls')),
    (r'^doctype/', include('doctype.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^myinfo/$', myinfo),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'dashboard.views.logout_view'),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
