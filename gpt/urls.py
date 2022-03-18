from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import os
from . import views

app_name = 'gpt'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('instalacoes/<int:pk>/', views.InstalacaoDetailView.as_view(), name='instalacao_detail'),
    path('documentos/', views.DocumentosView.as_view(), name='documentos_list'),
    path('instalacoes/', views.InstalacaoView.as_view(), name='instalacoes_list'),
    path('instalacoes/nova/', views.InstalacaoCreateView.as_view(), name='instalacoes_create'),
    path('instalacoes/<int:pk>/atualizar/', views.InstalacaoUpdateView.as_view(), name='instalacoes_update'),
    path('instalacoes/<int:pk>/excluir/', views.InstalacaoDeleteView.as_view(), name='instalacoes_delete'),
    path('documentos/<int:pk>/', views.DocumentoDetailView.as_view(), name='documento_detail'),
    path('documentos/novo/', views.DocumentoCreateView.as_view(), name='documentos_create'),
    path('documentos/<int:pk>/atualizar/', views.DocumentoUpdateView.as_view(), name='documentos_update'),
    path('instcomplete/', views.InstalacaoAutocomplete.as_view(), name='instalacao_autocomplete'),
]


