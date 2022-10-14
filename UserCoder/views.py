from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from AppCoder.views import *
from UserCoder.forms import *
from UserCoder.models import MasDatosUsuario


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

    return render(request, "UserCoder/login.html", {'form': form})


def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html', {})
        else:
            return render(request, 'UserCoder/register.html', {'form': form})

    form = MyUserCreationForm()
    return render(request, 'UserCoder/register.html', {'form': form})

def perfil(request):

    return render(request, 'UserCoder/perfil.html', )

def editar_perfil(request):

    user = request.user
    mas_datos_usuario, _ = MasDatosUsuario.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user.first_name = data.get('first_name') if data.get(
                'first_name') else user.first_name

            user.last_name = data.get('last_name') if data.get(
                'last_name') else user.last_name
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuario.avatar = data.get('avatar') if data.get(
                'avatar') else mas_datos_usuario.avatar

            mas_datos_usuario.descripcion = data.get('descripcion') if data.get(
                'descripcion') else mas_datos_usuario.descripcion

            mas_datos_usuario.link = data.get('link') if data.get('link') else mas_datos_usuario.link

            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password(data.get('password1'))

            mas_datos_usuario.save()
            user.save()

            return redirect('perfil')

        else:
            return render(request, 'UserCoder/editar_perfil', {'form': form})

    form = MyUserEditForm(initial={'email': user.email,
                                   'first_name': user.first_name,
                                   'last_name': user.last_name,
                                   'avatar': mas_datos_usuario.avatar,
                                   'descripcion': mas_datos_usuario.descripcion,
                                   'link': mas_datos_usuario.link,
                                   })

    return render(request, 'UserCoder/editar_perfil.html', {'form': form})