from django.contrib import admin
from .models import Registrado
from .forms import RegistradoForm

# Register your models here.


class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__srt__","dni","direccion","provincia","fecha_nacimiento","iniciado","actualizado"]
	form = RegistradoForm
	# class Meta:
	# 	model = Registrado


admin.site.register(Registrado, AdminRegistrado)
