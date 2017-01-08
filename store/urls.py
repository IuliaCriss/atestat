from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.home, name='home'),
				url(r'^contact$', views.contact, name='contact'),
				url(r'^categorii/(?P<stringCategorie>.+)/$', views.listeazaCarti, name='categorie'),
				url(r'^categorii$', views.categorii, name='categorii'),
				url(r'^categorii/(?P<stringCategorie>.+)/(?P<idCarte>\d+)$', views.detaliiCarte, name='carte'),





				]