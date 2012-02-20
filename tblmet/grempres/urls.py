from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('grempres.views',
    # Examples:
    # url(r'^$', 'ttso.views.home', name='home'),
    # url(r'^ttso/', include('ttso.foo.urls')),
    url (r'^empreendimento/', 'cademp', name='cademp'),
    url (r'^empresas/', 'cadmpa', name='cadmpa'),
    url (r'^pessoas/', 'cadpes', name='cadpes'),
    url (r'^(\d+)/sucesso/$', 'success',  name='success'), 
    url (r'^(\d+)/delete/$', 'delete',  name='delete'),
    #url (r'^dumpall/', 'dumpall',  name='dumpall'),
    #url(r'^/')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
