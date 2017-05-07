from __future__ import unicode_literals
from django.db import models

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
	autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
	categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
	descriere = models.TextField()
	recenzie = models.TextField()
	nota = models.DecimalField(max_digits = 2, decimal_places = 1)

	def __str__(self):
		return self.titlu

class Cerere(models.Model):

	nume = models.CharField(max_length=200)
	autor = models.CharField(max_length=200)
	titlu = models.CharField(max_length=200)

	def __str__(self):
		return self.titlu