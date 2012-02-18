#-*- coding: utf-8 -*-

from grmetodos.models import *
from django.contrib import admin

admin.site.register([TblAtribs,TblUnidades,TblLocais,TblApetrechos,TblMetodos,
TblAtrEts,TblInstrumentais, TblMetIns, TblMetAtEts])
