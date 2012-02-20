#-*- coding: utf-8 -*-

from grmetodos.models import *
from django.contrib import admin
from grempres.models import TblEmpreendimentos,  TblEmpresas,  TblPessoas
from gratributos.models import *
from grdados.models import *

admin.site.register([ TblUnidades, TblAtribs, TblLocais,  TblEmpreendimentos, TblEmpresas, TblPessoas])
