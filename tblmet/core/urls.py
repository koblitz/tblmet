from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tblmet.views.home', name='home'),
    # url(r'^tblmet/', include('tblmet.foo.urls')),
    #url (r'^caracterize-esforco-espaco/', 'meatun',  name='meatun'),
    #url (r'^(\d+)/deletado/$', 'core.views.delete',  name='delete'), 

     
     #(r'^con/',  include ('consultas.urls',  namespace='consultas')), 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
