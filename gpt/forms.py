from django import forms
from django.forms import ModelForm
from .models import Documento
from dal import autocomplete
import djhacker
from django import forms

djhacker.formfield(
    Documento.instalacoes,
    forms.ModelChoiceField,
    widget= autocomplete.ModelSelect2Multiple(url='gpt:instalacao_autocomplete')
)

'''
class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = ['origem','tipo','codigo','titulo','data_doc','instalacoes','referencias','arquivo']
        widgets = {
            'instalacoes': autocomplete.ModelSelect2Multiple(url='gpt:instalacao_autocomplete')
        }

'''