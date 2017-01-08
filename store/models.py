from __future__ import unicode_literals
from django.db import models
from django.utils import timezone



class Categorie(models.Model):

	nume = models.CharField(max_length=200)


	def __str__(self):
		return self.nume


class Autor(models.Model):
	nume = models.CharField(max_length=300)

	def  __str__(self):
		return self.nume

class Carte(models.Model):

	titlu = models.CharField(max_length=200)
	pret = models.PositiveIntegerField()
	descriere = models.TextField()
	categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
	autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
	stoc = models.PositiveIntegerField()

	def vinde(self):
		self.stoc -= 1

	def __str__(self):
		return self.titlu