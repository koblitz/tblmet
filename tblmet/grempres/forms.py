#-*- coding: utf-8 -*-
from django import forms
from grempres.models import TblEmpreendimentos
from grempres.models import TblEmpresas
from grempres.models import TblPessoas


class TblEmpreendimentosForm(forms.ModelForm):
            
    class Meta:
        model = TblEmpreendimentos
        exclude=('id_empreendimento',)
        
class TblEmpresasForm(forms.ModelForm):
    class Meta:
        model = TblEmpresas
        
class TblPessoasForm(forms.ModelForm):
    class Meta:
        model=TblPessoas
    
