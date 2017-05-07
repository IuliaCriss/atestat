from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.home, name='home'),
				url(r'^contact$', views.contact, name='contact'),
				url(r'^categorii/(?P<stringCategorie>.+)/(?P<idCarte>\d+)$', views.detaliiCarte, name='carte'),
				url(r'^categorii/(?P<stringCategorie>.+)/$', views.listeazaCartiCat, name='categorie'),
				url(r'^categorii$', views.categorii, name='categorii'),
				url(r'^autori/(?P<stringAutor>.+)/(?P<idCarte>\d+)$', views.detaliiCarte, name='carte'),
				url(r'^autori/(?P<stringAutor>.+)/$', views.listeazaCartiAut, name='autor'),
				url(r'^autori$', views.autori, name='autori'),
				url(r'^cerere$', views.cerere, name='cerere'),

				]