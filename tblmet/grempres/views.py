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

def cademp(request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    d=TblEmpreendimentos()
    h=TblEmpreendimentos
    i=' Empreendimentos'
    form= TblEmpreendimentosForm()
    f=TblEmpreendimentosForm(request.POST)
    a=TblEmpreendimentosManager()
    c='nome, processo, descricao'
    b=a.sulta()
    bb=a.sultaid()
    
    return inemp(request)
def cadmpa(request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    d=TblEmpresas()
    h=TblEmpresas
    i=' Empresas'
    form= TblEmpresasForm()
    f=TblEmpresasForm(request.POST)
    a=TblEmpresasManager()
    c='nome, descricao'
    b=a.sulta()
    bb=a.sultaid()
    return inemp(request)
def cadpes(request):
    global h,  form,  f, i,  a,  b,  d,  c,  bb
    d=TblPessoas()
    h=TblPessoas
    i=' Pessoas'
    form= TblPessoasForm()
    f=TblPessoasForm(request.POST)
    a=TblPessoasManager()
    c='nome, processo, descricao'
    b=a.sulta()
    bb=a.sultaid()
    return inemp(request)
def inemp(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new (request):
    
    return direct_to_template(request, 'inemp_new.html', {
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
        return render_to_response('inemp_new.html', context)
    inemp=form.save()
    return HttpResponseRedirect(
    reverse('grempres:success', args=[ inemp.pk ]))

def success (request, pk):
    inemp = get_object_or_404(h, pk=pk)
    d=h.objects.filter(id=inemp.id)
#    consulta = RequestContext(request,  {'d':d})
#    context = RequestContext(request, {'inmet': inmet})
    return render_to_response('inemp_success.html',  {'d':d, 'inemp':inemp})

def delete (request, pk):
    inemp=get_object_or_404(h, pk=pk)
    a=h.objects.filter(id=inemp.id).delete()
#   consulta = RequestContext(request,  )
#    context = RequestContext(request, {'inmet': inmet})
    return render_to_response('inemp_delete.html',  {'a':a,  'inemp':inemp})
 #   return HttpResponseRedirect('inmet_new.html')
