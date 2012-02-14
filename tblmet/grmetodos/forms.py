#-*- coding: utf-8 -*-
from django import forms
from grmetodos.models import TblUnidades
from grmetodos.models import TblAtribs
from grmetodos.models import TblMetodos
from grmetodos.models import TblApetrechos
from grmetodos.models import TblAtrEts
from grmetodos.models import TblInstrumentais
from grmetodos.models import TblMetIns
from grmetodos.models import TblMetAtEts
from grmetodos.models import TblLocais


class TblUnidadesForm(forms.ModelForm):
            
    class Meta:
        model = TblUnidades

class TblAtribsForm(forms.ModelForm):
    class Meta:
        model = TblAtribs
        
class TblLocaisForm(forms.ModelForm):
    class Meta:
        model=TblLocais
        
class TblMetodosForm(forms.ModelForm):
    class Meta:
        model=TblMetodos
        
class TblApetrechosForm(forms.ModelForm):
    class Meta:
        model=TblApetrechos
        
class TblAtrEtsForm(forms.ModelForm):
    class Meta:
        model=TblAtrEts

class TblInstrumentaisForm(forms.ModelForm):
    class Meta:
        model=TblInstrumentais

class TblMetInsForm(forms.ModelForm):
    class Meta:
        model=TblMetIns
        
class TblMetAtEtsForm(forms.ModelForm):
    class Meta:
        model=TblMetAtEts
