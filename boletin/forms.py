
from django import forms

from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre","apellido","dni","fecha_nacimiento","direccion","provincia",]


	# def clean_nombre(self):
	# 	model = Registrado
	# 	valor = self.cleaned_data["nombre"]
	# 	if model.objects.filter(nombre=valor).exists():
	# 		raise forms.ValidationError("El usuario ya existe")
	# 	return valor

	def clean_dni(self):
		model = Registrado
		valor = self.cleaned_data["dni"]
		if model.objects.filter(dni=valor).exists():
			raise forms.ValidationError("Este Numero de DNI ya esta en uso")
		return valor
			





