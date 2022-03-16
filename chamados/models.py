from datetime import datetime
from django.db import models

# Create your models here.

class Usuario(models.Model):
    #titulo_eleitoral = models.CharField(max_length=12)
    nome = models.CharField(max_length=150)
    #foto_usuario = models.ImageField(upload_to='figuras/%Y-%m-%d',blank=True)
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.categoria

class Fila(models.Model):
    fila = models.CharField(max_length=30)
    def __str__(self):
        return self.fila

class Estado(models.Model):
    estado = models.CharField(max_length=30)
    def __str__(self):
        return self.estado

class Prioridade(models.Model):
    prioridade = models.CharField(max_length=30)
    def __str__(self):
        return self.prioridade

class Chamado(models.Model):
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    fila = models.ForeignKey(Fila,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    numero_chamado = models.IntegerField()
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    patrimonio = models.CharField(max_length=10, blank=True)
    ip = models.CharField(max_length=15, blank=True)
    prioridade = models.ForeignKey(Prioridade,on_delete=models.CASCADE)
    data = models.DateTimeField(default=datetime.now)
    figura_chamado = models.ImageField(upload_to='figuras/%Y-%m-%d',blank=True)
    def __str__(self):
        exibe = "Chamado #"
        numero_chamado_string = str(self.numero_chamado)
        return exibe+numero_chamado_string