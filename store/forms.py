from django import forms
from .models import Cerere

class CerereForm(forms.ModelForm):

	class Meta:
		model = Cerere
		fields = ('nume','autor','titlu')