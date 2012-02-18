from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('grmetodos.views',
    # Examples:
    # url(r'^$', 'ttso.views.home', name='home'),
    # url(r'^ttso/', include('ttso.foo.urls')),
    url (r'^unidade/', 'uni', name='uni'),
    url (r'^atributo/', 'atr', name='atr'),
    url (r'^metodo/', 'met', name='met'),
    url (r'^apetrecho/', 'ape',  name='ape'),
    url (r'^local/', 'loc',  name='loc'),
    url (r'^atributos-estacoes/', 'atrest',  name='atrest'),
    url (r'^caracteriza-apetrecho/', 'int',  name='int'),
    url (r'^quantidade_apetrecho-por-estacao/', 'metint',  name='metint'), 
    url (r'^caracterize-esforco-espaco/', 'meatun',  name='meatun'),    
    url (r'^(\d+)/sucesso/$', 'success',  name='success'), 
    url (r'^(\d+)/delete/$', 'delete',  name='delete'),
    
    #url(r'^/')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
