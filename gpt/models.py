from django.conf import settings
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

def choiceToString(choice, choiceList):
    for c in choiceList:
        if c[0] == choice:
            return c[1]
    return ''    


class Instalacao(models.Model):
    RECIFE = 'BGI'
    NATAL = 'NTD'
    SALVADOR = 'PTU'
    FORTALEZA = 'FTZ'
    SOBRADINHO = 'SBD'
    PAULO_AFONSO = 'PAF'
    REGIONAL_CHOICES = [
        (RECIFE, 'Recife'),
        (NATAL, 'Natal'),
        (SALVADOR, 'Salvador'),
        (FORTALEZA, 'Fortaleza'),
        (SOBRADINHO, 'Sobradinho'),
        (PAULO_AFONSO, 'Paulo Afonso'),
    ]
    USINA = 'US'
    SE = 'SE'
    TIPO_CHOICES = [
        (USINA, 'Usina'),
        (SE, 'Subestação')
    ]
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=3, unique=True)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default=SE)
    regional = models.CharField(max_length=3, choices=REGIONAL_CHOICES, default=RECIFE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('-criado_em',)

    def get_absolute_url(self):
        return reverse('gpt:instalacao_detail', kwargs={'pk': self.pk})
    
    @property
    def get_tipo(self):
        return choiceToString(self.tipo, self.TIPO_CHOICES)
    
    @property
    def get_regional(self):
        return choiceToString(self.regional, self.REGIONAL_CHOICES)
    
    def __str__(self):
        return self.sigla


class Origem(models.Model):
    REGULADOR = 'RG'
    GOVERNO = 'GV'
    INTERNO = 'CH'
    FORNECEDOR = 'FN'
    OUTRO = 'OU'
    TIPO_ORIGEM_CHOICES = [
        (REGULADOR, 'Órgão regulador'),
        (GOVERNO, 'Órgão governamental'),
        (INTERNO, 'Órgão interno Chesf'),
        (FORNECEDOR, 'Fornecedor'),
        (OUTRO, 'Outro')
    ]

    sigla = models.CharField(max_length=50)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=2, choices=TIPO_ORIGEM_CHOICES, default=INTERNO)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('-criado_em',)
    
    @property
    def get_tipo(self):
        return choiceToString(self.tipo, self.TIPO_ORIGEM_CHOICES)

    def __str__(self):
        return self.sigla
    


class Documento(models.Model):
    REA = 'RA'
    R4 = 'R4'
    OFICIO = 'OF'
    NT = 'NT'
    PRORET = 'PR'
    DESPACHO = 'DP'
    ET = 'ET'
    OUTRO = 'OU'
    TIPO_DOC_CHOICES = [
        (REA, 'Resolução Autorizativa'),
        (R4, 'Relatório R4'),
        (OFICIO, 'Ofício'),
        (NT, 'Nota Técnica'),
        (PRORET, 'Relatório PRORET'),
        (DESPACHO, 'Despacho'),
        (ET, 'Especificação Técnica'),
        (OUTRO, 'Outro')
    ]

    origem = models.ForeignKey(Origem, on_delete=models.SET_NULL, related_name='documentos', blank=True, null=True)
    tipo = models.CharField(max_length=2, choices=TIPO_DOC_CHOICES)
    codigo = models.CharField(max_length=50, verbose_name='código')
    titulo = models.CharField(max_length=200, verbose_name='título')
    data_doc = models.DateField('data do documento', blank=True, null=True)
    instalacoes = models.ManyToManyField(Instalacao, blank=True, verbose_name='instalações', related_name='documentos')
    referencias = models.ManyToManyField('self', blank=True, verbose_name='referências')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='documentos')
    arquivo = models.FileField(upload_to='arq', null=True, blank=True)

    class Meta:
        ordering = ('-criado_em',)
    
    def get_absolute_url(self):
        return reverse('gpt:documento_detail', kwargs={'pk': self.pk})
    
    @property
    def get_filename(self):
        if self.arquivo:
            try:
                return self.arquivo.name.rsplit('/')[1]
            except:
                return self.arquivo.name
        return ''
    
    @property
    def get_tipo(self):
        return choiceToString(self.tipo, self.TIPO_DOC_CHOICES)

    def __str__(self):
        return  '{} - {} - {}'.format(self.origem, self.codigo, self.titulo)






