from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
        path('',views.index_g,name='index_g'),
        path('login/',views.login,name='login'),
        path('cadastro/',views.cadastro,name='cadastro'),
]