from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index,  name='index'),
    path('index', views.index,  name='index'),
    path('<int:id>', views.detalhe_chamado,  name='detalhe_chamado'),
    path('article', views.article,  name='article'),
    path('terms', views.terms,  name='terms'),
    path('privacy', views.privacy,  name='privacy'),
    path('chamados', views.chamados,  name='chamados')
    
]