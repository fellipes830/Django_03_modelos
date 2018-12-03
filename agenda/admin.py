from django.contrib import admin

from .models import ItemAgenda

class AgendaAdmin(admin.ModelAdmin):
	list_display = ('data','hora','titulo','descricao')

admin.site.register(ItemAgenda, AgendaAdmin)	
