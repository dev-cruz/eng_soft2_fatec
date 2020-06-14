# -*- coding: utf-8 -*-
from core import menu_mixin
from tools.views import base as tools_views
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from vagas.forms import (VagaForm, VagaSearchForm,
                         CompetenciaForm, CompetenciaSearchForm)
from vagas.models import (Vaga, Competencia)


class VagaListView(
    menu_mixin.ProjetoMenuMixin,
    tools_views.BaseListView
):
    filter_by_user = False
    permission_required = ''
    form_class = VagaSearchForm
    current_section = 'vagas'
    sub_current_section = 'vagas'


class VagaCreateView(
    menu_mixin.ProjetoMenuMixin,
    tools_views.BaseCreateView
):
    filter_by_user = False
    permission_required = ''
    current_section = 'vagas'
    sub_current_section = 'vagas'
    model = Vaga
    form_class = VagaForm

    def addcompetencia(request):
        competencia = Competencia.objects.all()
        if request.method == 'POST':
            form = VagaForm(request.POST,request.FILES)
            if form.is_valid():
                vaga = form.save(commit=True)
                competencia = form.cleaned_data['competencia']
                vaga.competencia = competencia
                beneficio = form.cleaned_data['beneficio']
                vaga.beneficio = beneficio
                vaga.save()


class VagaUpdateView(
    menu_mixin.ProjetoMenuMixin,
    tools_views.BaseUpdateView
):
    filter_by_user = False
    detail_url = False
    permission_required = ''
    current_section = 'vagas'
    sub_current_section = 'vagas'
    model = Vaga
    form_class = VagaForm

    def addcompetencia(request):
        competencia = Competencia.objects.all()
        if request.method == 'POST':
            form = VagaForm(request.POST,request.FILES)
            if form.is_valid():
                vaga = form.save(commit=True)
                competencia = form.cleaned_data['competencia']
                vaga.competencia = competencia
                beneficio = form.cleaned_data['beneficio']
                vaga.beneficio = beneficio
                vaga.save()


class CompetenciaListView(
    menu_mixin.ProjetoMenuMixin,
    tools_views.BaseListView
):
    filter_by_user = False
    permission_required = ''
    form_class = CompetenciaSearchForm
    current_section = 'vagas'
    sub_current_section = 'competencias'


class CompetenciaCreateView(
    menu_mixin.ProjetoMenuMixin,
    tools_views.BaseCreateView
):
    filter_by_user = False
    permission_required = ''
    current_section = 'vagas'
    sub_current_section = 'competencias'
    model = Competencia
    form_class = CompetenciaForm

class CompetenciaUpdateView(
    menu_mixin.ProjetoMenuMixin,
    tools_views.BaseUpdateView
):
    filter_by_user = False
    detail_url = False
    permission_required = ''
    current_section = 'vagas'
    sub_current_section = 'competencias'
    model = Competencia
    form_class = CompetenciaForm