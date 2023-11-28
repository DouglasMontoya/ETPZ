# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import datetime, decimal
from itertools import count
from multiprocessing import context
from urllib import request
from django import template
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template import loader
from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, permission_required

from .models import *
from .forms import *

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

#----------------------------------------------------------------------------------

def periodos(request):
    periodos = Periodo.objects.all().annotate(num_estudiantes=Count('estudiante'))

    context={
        'periodos':periodos,
        'segment':'periodo',
        'title':'Periodos',
        'table':'home/table-content/periodos.html',
    }

    return render(request, 'home/table.html', context)


def carga_notas(request, pd):
    
    periodo = get_object_or_404(Periodo, pk=pd)
    carga = periodo.carga
    materias = carga.materias.all().order_by("nombre")
    estudiantes = Estudiante.objects.filter(periodo=periodo).order_by("ci")
    print(estudiantes)
    print(materias)
    cantidad_materias = materias.count()
    total_forms = cantidad_materias * estudiantes.count()
    print(total_forms)
    
    formset = formset_factory(NotasForm, extra=total_forms)
    formset(request.POST or None)
    
    context = {
        'periodo': periodo,
        'carga': carga,
        'materias': materias,
        'cantidad_materias': cantidad_materias,
        'estudiantes': estudiantes,
        'formset': formset,
        'segment': 'carga'
        }

    return render(request, 'home/carga_de_notas.html', context)
