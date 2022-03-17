from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index,  name='index'),
    path('index', views.index,  name='index'),
    path('<int:id>', views.detalhe_chamado,  name='detalhe_chamado'),
    path('detalhe_chamado_ajax/<int:id>', views.detalhe_chamado_ajax,name='detalhe_chamado_ajax'),
    path('article', views.article,  name='article'),
    path('terms', views.terms,  name='terms'),
    path('privacy', views.privacy,  name='privacy'),
    path('chamados', views.chamados,  name='chamados'),
    path('chamados_ajax', views.chamados_ajax,  name='chamados_ajax'),
    path('chamados_ajax2', views.chamados_ajax2,  name='chamados_ajax2')
    
]