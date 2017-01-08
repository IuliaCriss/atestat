from django.shortcuts import render
from .models import Categorie, Carte

# Create your views here.
def home(request):
	return render(request, 'home.html')

def contact(request):
	return render(request, 'contact.html')

def categorii(request):
	categorii = Categorie.objects.all()  
	informatie = {
			"categorii": categorii
	}
	return render(request, 'categorii.html', informatie)

def listeazaCarti(request, stringCategorie):

	cat = Categorie.objects.filter(nume=stringCategorie)[0]
	carti = Carte.objects.filter(categorie=cat)
	informatie = {
			"carti": carti
	}
	return render(request, 'listaCarti.html', informatie)

def detaliiCarte(request, stringCategorie, idCarte):
	carte = Carte.objects.get(pk=idCarte)
	informatie = {
			"carte": carte
	}
	return render(request, 'detaliiCarte.html', informatie)



