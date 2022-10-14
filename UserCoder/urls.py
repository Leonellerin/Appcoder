from django.contrib.auth.views import LogoutView
from django.urls import path

from UserCoder.views import *

urlpatterns = [
    path('login/', login_request, name='UserCoderLogin'),

    path('logout/', LogoutView.as_view(template_name='UserCoder/logout.html'), name='UserCoderLogout'),

    path('register/', register, name='UserCoderRegister'),

    path('perfil/', perfil, name='perfil'),

    path('editar_perfil/', editar_perfil, name='editar_perfil'),



]