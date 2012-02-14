from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('consultas.views',
    # Examples:
    # url(r'^$', 'ttso.views.home', name='home'),
    # url(r'^ttso/', include('ttso.foo.urls')),
    url (r'^plano-trabalho/', 'platrb',  name='platrb'),
    url (r'^atributo-csv/', 'uatrsulta', name='uatrsulta'),
    url (r'^caracteriza-esforco-espaco-csv', 'umetatetssulta', name='umetatetssulta'),
    url (r'^unidade-csv/', 'uunisulta', name='uunisulta'),
    url (r'^apetrecho-csv/', 'uapesulta', name='uapesulta'),
    url (r'^metodo-csv/', 'umetsulta',  name='umetsulta'),
    url (r'^atributos-estacoes-csv', 'uatretssulta',  name='uatretssulta'),
    url (r'^caracteriza-apetrechos-csv/', 'uinssulta',  name='uinssulta'),
    url (r'^quantidade_apetrechos-p-estacao-csv/', 'umetinssulta',  name='umetinssulta'),
    
    #url (r'^(\d+)/sucesso/$', 'success',  name='success')
    
    #url(r'^/')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
