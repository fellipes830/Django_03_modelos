from django.contrib import admin

from .models import *

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','matricula','data_nascimento')


class EmprestimoAdmin(admin.ModelAdmin):
	list_display = ('data_devolucao','data_retirada','aluno','devolvido')
	filter_horizontal = ['livros']


admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
