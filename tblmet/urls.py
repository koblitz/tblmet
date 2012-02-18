#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    # Examples:
    # url(r'^$', 'tblmet.views.home', name='home'),
    # url(r'^tblmet/', include('tblmet.foo.urls')),
    url (r'^$',  'direct_to_template', {'template':'index.html'}), 
     (r'^operacoes/',  include ('grmetodos.urls', namespace= 'grmetodos')),
     (r'^consultas/',  include ('consultas.urls', namespace= 'consultas')),
     #(r'^operacoes/',  include ('core.urls', namespace='core')), 

     
     #(r'^con/',  include ('consultas.urls',  namespace='consultas')), 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
