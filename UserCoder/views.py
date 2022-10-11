from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from AppCoder.views import *

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/busqueda_camada.html", {"mensaje": f"Bienvenido {usuario}"})
            else:

                return render(request, "AppCoder/busqueda_camada.html", {"mensaje": "Error, datos incorrectos"})

        else:

            return render(request, "AppCoder/busqueda_camada.html", {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {'form': form})
