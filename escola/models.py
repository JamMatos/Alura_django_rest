from django.db import models

# Create your models here.
class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, blank=False)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL_ESCOLHA = [
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    ]

    code = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL_ESCOLHA, default='B', blank=False, null=False)

    def __str__(self):
        return self.code

