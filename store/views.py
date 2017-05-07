from django.shortcuts import render,redirect
from .models import Categorie, Carte, Autor
from .forms import CerereForm
# Create your views here.

def home(request):
	bestRated = ordered_authors = Carte.objects.order_by('-nota')[:5]

	listaCarti = []
	i = 1
	for carte in bestRated:
		listaCarti.append({
				'nr':i,
				'carte':carte,
			})
		i += 1
	informatie = {
				"carti" : listaCarti
	}
	return render(request, 'home.html', informatie)

def contact(request):
	return render(request, 'contact.html')

def categorii(request):
	categorii = Categorie.objects.all()  
	informatie = {
			"categorii": categorii
	}
	return render(request, 'categorii.html', informatie)

def listeazaCartiCat(request, stringCategorie):

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



def autori(request):
	autori = Autor.objects.all()  
	informatie = {
			"autori": autori
	}
	return render(request, 'autori.html', informatie)

def listeazaCartiAut(request, stringAutor):

	aut = Autor.objects.filter(nume=stringAutor)[0]
	carti = Carte.objects.filter(autor=aut)
	informatie = {
			"carti": carti
	}
	return render(request, 'listaCarti.html', informatie)

def cerere(request):
	if request.method == "GET":
		form  = CerereForm()
		informatie = {
					'form': form
		}
		return render(request, 'cerere.html', informatie)
	else:
		form = CerereForm(request.POST)
		if form.is_valid():
			cerere = form.save(commit=False)
			cerere.save()
			return redirect("home")