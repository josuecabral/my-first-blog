from django.shortcuts import render
from .forms import RegistradoForm
from .forms import Registrado

# Create your views here.

def inicio(request):
	titulo = "Bienvenido"
	form = RegistradoForm(request.POST or None)
	queryset=Registrado.objects.all()

	

	context = {
		"titulo":titulo,
		"form":form,
		"queryset":queryset,
	}


	if form.is_valid():
		form.save()

		nombre = form.cleaned_data.get("nombre")
		ndni = form.cleaned_data.get("dni")
		context={
			"titulo": "Gracias %s ya se ha registrado." %(nombre)
		}
		if not nombre:
			context={
			"titulo": "Gracias %s ya se ha registrado." %(dni)
		}


	


	return render(request,"inicio.html",context)


# def sobre(request):
# 	titulo = "Sobre Nosotros"

# 	context = {
# 		"titulo":titulo,
# 	}


	


# 	return render(request,"sobre.html",context)





def registrados(request):
	titulo = "Registrados"
	queryset=Registrado.objects.all()

	context = {
		"titulo": titulo,
		"queryset":queryset,
	}


	return render(request, "registrados.html", context)
