from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def index_g(request):
    return render(request, 'index_g.html')