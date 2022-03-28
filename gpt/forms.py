from django import forms
from django.forms import ModelForm
from .models import Documento
from dal import autocomplete
import djhacker
from django import forms

djhacker.formfield(
    Documento.referencias,
    forms.ModelMultipleChoiceField,
    widget= autocomplete.ModelSelect2Multiple(url='gpt:doc-autocomplete')
)


class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = ['origem','tipo','codigo','titulo','data_doc','instalacoes','referencias','arquivo']
        widgets = {
            'referencias': autocomplete.ModelSelect2Multiple(url='gpt:doc-autocomplete')
        }

