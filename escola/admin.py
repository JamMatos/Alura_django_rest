from django.contrib import admin
from escola.models import Estudante, Curso

# Register your models here.
class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email','cpf','data_nascimento','celular')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome','cpf')
    ordering = ('nome',)

admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'code', 'descricao')
    list_display_links = ('id', 'code',)
    search_fields = ('code',)

admin.site.register(Curso, Cursos)