from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
