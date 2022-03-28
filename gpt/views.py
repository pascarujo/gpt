from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Documento, Instalacao
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy
from dal import autocomplete
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import DocumentoForm


# from .forms import DocumentoForm
# import gpt.forms

# Create your views here.

@method_decorator(login_required, name='dispatch')
class InstalacaoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Instalacao.objects.all()
        if self.q:
            qs = qs.filter(nome__istartswith=self.q)
        return qs

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    login_required = True
    template_name = 'gpt/index.html'
    context_object_name = 'latest_instalacao_list'
    paginate_by = 50

    def get_queryset(self):
        return Instalacao.objects.order_by('-criado_em')

@method_decorator(login_required, name='dispatch')
class InstalacaoView(generic.ListView):
    login_required = True
    template_name = 'gpt/instalacoes_list.html'
    context_object_name = 'instalacoes_list'
    paginate_by = 50

    def get_queryset(self):
        return Instalacao.objects.order_by('-criado_em')

@method_decorator(login_required, name='dispatch')
class DocumentosView(generic.ListView):
    login_required = True
    template_name = 'gpt/documentos_list.html'
    context_object_name = 'documentos_list'
    paginate_by = 50

    def get_queryset(self):
        return Documento.objects.order_by('-criado_em')

@method_decorator(login_required, name='dispatch')
class InstalacaoDetailView(generic.DetailView):
    login_required = True
    model = Instalacao
    template_name = 'gpt/instalacao_detail.html'

@method_decorator(login_required, name='dispatch')
class DocumentoDetailView(generic.DetailView):
    login_required = True
    model = Documento
    template_name = 'gpt/documento_detail.html'


@method_decorator(login_required, name='dispatch')
class InstalacaoCreateView(CreateView):
    login_required = True
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


@method_decorator(login_required, name='dispatch')
class InstalacaoUpdateView(UpdateView):
    login_required = True
    model = Instalacao
    fields = ['sigla','nome','regional','tipo']
    success_url = reverse_lazy('gpt:instalacoes_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo"] = 'update'
        return context


@method_decorator(login_required, name='dispatch')
class InstalacaoDeleteView(DeleteView):
    login_required = True
    model = Instalacao
    success_url = reverse_lazy('gpt:instalacoes_list')



@method_decorator(login_required, name='dispatch')
class DocumentoCreateView(CreateView):
    login_required = True
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


@method_decorator(login_required, name='dispatch')
class DocumentoUpdateView(UpdateView):
    login_required = True
    model = Documento
    fields = ['origem','tipo','codigo','titulo','data_doc','instalacoes','referencias','arquivo']
    success_url = reverse_lazy('gpt:documentos_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo"] = 'update'
        return context
    

class DocumentoAutocomplete(autocomplete.Select2QuerySetView):
     def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Documento.objects.none()

        qs = Documento.objects.all()

        if self.q:
            qs = qs.filter(titulo__istartswith=self.q)

        return qs


class DocumentoTeste(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'gpt/teste.html'
    # fields = ['origem','tipo','codigo','titulo','data_doc','instalacoes','referencias','arquivo']
    success_url = reverse_lazy('gpt:documentos_list')
    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo"] = 'create'
        return context