#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response,  get_object_or_404
from django.template import RequestContext
from forms import *
from models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.http import HttpResponse
from django.template	import loader, Context

#from django.utils.encoding import encode
    
def uni (request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    d=TblUnidades()
    h=TblUnidades
    i=' Unidades'
    form= TblUnidadesForm()
    f=TblUnidadesForm(request.POST)
    a=TblUnidadesManager()
    c='unidade, nome, descricao'
    b=a.sulta()
    bb=a.sultaid()
    
    return inmet(request)
def loc(request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    d=TblLocais()
    h=TblLocais
    i='Locais'
    form= TblLocaisForm()
    f=TblLocaisForm(request.POST)
    a=TblLocaisManager()
    c='local, descricao'
    b=a.sulta()
    bb=a.sultaid()
    return inmet(request)
    
def atr(request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    d=TblAtribs()
    h=TblAtribs
    i='Atributos'
    form= TblAtribsForm()
    f=TblAtribsForm(request.POST)
    a=TblAtribsManager()
    c='medida, nome, descricao'
    b=a.sulta()
    bb=a.sultaid()
    return inmet(request)

def met(request):
    global h,  form,  f, i,  a,  b,  d, c,  bb
    d=TblMetodos()
    h=TblMetodos
    i='Métodos'
    form=TblMetodosForm()
    f=TblMetodosForm(request.POST)
    a=TblMetodosManager()
    c='metodo, nome, obs'
    b=a.sulta()
    bb=a.sultaid()
    return inmet(request)
    
def ape(request):
    global h, form, f, i, a, b, d, c,  bb
    i='Apetrechos'
    h=TblApetrechos
    d=TblApetrechos()
    form=TblApetrechosForm()
    f=TblApetrechosForm(request.POST)
    a=TblApetrechosManager()
    c='apetrecho, nome, descricao'
    b=a.sulta()
    bb=a.sultaid()
    return inmet(request)

def atrest(request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    i='Atributos de Estação'
    h=TblAtrEts
    d=TblAtrEts()
    form=TblAtrEtsForm()
    f=TblAtrEtsForm(request.POST)
    a=TblAtrEtsManager()
    c='medida, nome, descrição'
    b=a.sulta()
    bb=a.sultaid()
    return inmet(request)

def int(request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    i= 'Características por Apetrecho'
    h=TblInstrumentais
    d=TblInstrumentais()
    form=TblInstrumentaisForm()
    f=TblInstrumentaisForm(request.POST)
    a=TblInstrumentaisManager()
    c='apetrecho, atributo,unidade'
    b=a.sulta()
    bb=a.sultaid()
    return inmet(request)

def metint(request):
    global h,  form,  f, i,  a,  b,  d, c,  bb
    i='Apetrechos por Estação'
    h=TblMetIns
    d=TblMetIns()
    form=TblMetInsForm()
    f=TblMetInsForm(request.POST)
    a=TblMetInsManager()
    c='metodo, apetrecho,quantidade'
    b=a.sulta()
    bb=a.sultaid()
    return inmet(request)

def meatun(request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    i= 'Características do Método'
    h=TblMetAtEts
    d=TblMetAtEts()
    form= TblMetAtEtsForm()
    f=TblMetAtEtsForm(request.POST)
    a=TblMetAtEtsManager()
    c='metodo, atributo_estacao, atributo, valor,unidade, obs'
    b=a.sulta()
    bb=a.sultaid()
    return inmet(request)
    
    
    
def inmet (request):

    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new (request):
    
    return direct_to_template(request, 'inmet_new.html', {
        'nome':'%s' %i, 
        'tbl': list(h.objects.all()), 
        'form': form, 
        'h':h, 
        'b':b,
        'bb':bb, 
        'c':c, 
         
        })

def create(request):
    form=f
    if not form.is_valid():
        context = RequestContext(request, {'form':form})
        return render_to_response('inmet_new.html', context)
    inmet=form.save()
    return HttpResponseRedirect(
    reverse('grmetodos:success', args=[ inmet.pk ]))

def success (request, pk):
    inmet = get_object_or_404(h, pk=pk)
    d=h.objects.filter(id=inmet.id)
#    consulta = RequestContext(request,  {'d':d})
#    context = RequestContext(request, {'inmet': inmet})
    return render_to_response('inmet_success.html',  {'d':d, 'inmet':inmet})

def delete (request, pk):
    inmet=get_object_or_404(h, pk=pk)
    a=h.objects.filter(id=inmet.id).delete()
#   consulta = RequestContext(request,  )
#    context = RequestContext(request, {'inmet': inmet})
    return render_to_response('inmet_delete.html',  {'a':a,  'inmet':inmet})
 #   return HttpResponseRedirect('inmet_new.html')

def dumpall(request):
    pass
    #    a='tblmet/seguranca/data.json'
#    response=dump(a)
    #response=HttpResponse(mimetype='text/javascript')
#    response['Content-Disposition']='attachment; filename=dump.json'
#    return response
