from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Documento, Instalacao
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy
from dal import autocomplete
# from .forms import DocumentoForm
# import gpt.forms

# Create your views here.

class InstalacaoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Instalacao.objects.all()
        if self.q:
            qs = qs.filter(nome__istartswith=self.q)
        return qs

class IndexView(generic.ListView):
    template_name = 'gpt/index.html'
    context_object_name = 'latest_instalacao_list'
    paginate_by = 50

    def get_queryset(self):
        return Instalacao.objects.order_by('-criado_em')

class InstalacaoView(generic.ListView):
    template_name = 'gpt/instalacoes_list.html'
    context_object_name = 'instalacoes_list'
    paginate_by = 50

    def get_queryset(self):
        return Instalacao.objects.order_by('-criado_em')


class DocumentosView(generic.ListView):
    template_name = 'gpt/documentos_list.html'
    context_object_name = 'documentos_list'
    paginate_by = 50

    def get_queryset(self):
        return Documento.objects.order_by('-criado_em')


class InstalacaoDetailView(generic.DetailView):
    model = Instalacao
    template_name = 'gpt/instalacao_detail.html'


class DocumentoDetailView(generic.DetailView):
    model = Documento
    template_name = 'gpt/documento_detail.html'


class InstalacaoCreateView(CreateView):
    model = Instalacao
    fields = ['sigla','nome','regional','tipo']

    success_url = reverse_lazy('gpt:instalacoes_list')
    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo"] = 'create'
        return context


class InstalacaoUpdateView(UpdateView):
    model = Instalacao
    fields = ['sigla','nome','regional','tipo']
    success_url = reverse_lazy('gpt:instalacoes_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo"] = 'update'
        return context

class InstalacaoDeleteView(DeleteView):
    model = Instalacao
    success_url = reverse_lazy('gpt:instalacoes_list')


class DocumentoCreateView(CreateView):
    model = Documento
    # form_class = DocumentoForm
    fields = ['origem','tipo','codigo','titulo','data_doc','instalacoes','referencias','arquivo']
    success_url = reverse_lazy('gpt:documentos_list')
    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo"] = 'create'
        return context
    
class DocumentoUpdateView(UpdateView):
    model = Documento
    fields = ['origem','tipo','codigo','titulo','data_doc','instalacoes','referencias','arquivo']
    success_url = reverse_lazy('gpt:documentos_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo"] = 'update'
        return context