import json
from random import random
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Chamado, Usuario 
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import random
# Create your views here.
def index(request):
    
    return render(request,'index.html')

def article(request):
    return render(request,'article.html')

def terms(request):
    return render(request,'terms.html')

def privacy(request):
    return render(request,'privacy.html')

def relatorios(request):
    chamados = Chamado.objects.all().order_by('-data')
    qtd = len(chamados)
    abertos = len(chamados.filter(estado=1))
    fechados = len(chamados.filter(estado=10))
    concluidos = len(chamados.filter(estado=7))
    aguardando = len(chamados.filter(estado=3))
    dados = {
        'total':qtd,
        'abertos':abertos,
        'fechados':fechados,
        'aguardando':aguardando,
        'concluidos':concluidos
        
    }
    return render(request,'relatorios.html', dados)

'''def chamados(request):
    chamados = Chamado.objects.all().order_by('-data')
    tamanho = len(chamados)
    paginador = Paginator(chamados,10)
    pagina = request.GET.get('pagina')
    chamados_por_pagina = paginador.get_page(pagina)
    dados = {
        'total':tamanho,
        'chamados': chamados_por_pagina
    }
    return render(request,'chamados.html', dados)

def detalhe_chamado(request,id):
    detalhe_chamado = Chamado.objects.get(id=id)
    conteudo = {'detalhe_chamado':detalhe_chamado}
    return render(request,'detalhe_chamado.html',conteudo)

def chamados_ajax(request):
    chamados = Chamado.objects.all().order_by('-data')
    tamanho = len(chamados)
    paginador = Paginator(chamados,10)
    pagina = request.GET.get('pagina')
    chamados_por_pagina = paginador.get_page(pagina)
    dados = {
        'total':tamanho,
        'chamados': chamados_por_pagina
    }
    return render(request,'chamados_ajax.html', dados)
'''    
def chamados_ajax2(request):
    chamados = Chamado.objects.all().order_by('-data')
    tamanho = len(chamados)
    paginador = Paginator(chamados,10)
    pagina = request.GET.get('pagina')
    chamados_por_pagina = paginador.get_page(pagina)
    dados = {
        'total':tamanho,
        'chamados': chamados_por_pagina
    }
    return render(request,'chamados_ajax2.html', dados)

def detalhe_chamado_ajax(request,id):
    detalhe_chamado = Chamado.objects.get(id=id)
    foto_usuario = str(random.randint(1,15))
    
    conteudo = {
        'detalhe_chamado':detalhe_chamado,
        'foto':foto_usuario
    }
    print(conteudo)
    return render(request,'detalhe_chamado_ajax.html',conteudo)

def chamados_ajax_col(request):
    chamados = Chamado.objects.all().order_by('-data')
    tamanho = len(chamados)
    paginador = Paginator(chamados,10)
    pagina = request.GET.get('pagina')
    chamados_por_pagina = paginador.get_page(pagina)
    dados = {
        'total':tamanho,
        'chamados': chamados_por_pagina
    }
    return render(request,'chamados_ajax_col.html', dados)

def detalhe_chamado_col(request,id):
    detalhe_chamado = Chamado.objects.get(id=id)
    foto_usuario = str(random.randint(1,15))
    
    conteudo = {
        'detalhe_chamado':detalhe_chamado,
        'foto':foto_usuario
    }
    print(conteudo)
    return render(request,'detalhe_chamado_col.html',conteudo)


#def detalhe_usuario(request,usuarioid):
#    detalhe_usuario = Usuario.objects.get(id=usuarioid)
#    conteudo_usuario = {'detalhe_usuario':detalhe_usuario}
#    return render(request,'detalhe_chamado.html',conteudo_usuario)