from django.db import models
import datetime
from django.utils import timezone

class ItemAgenda(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()

	def __str__(self):
		return self.data
	def __str__(self):
		return self.titulo
	def __str__(self):
		return self.descricao
