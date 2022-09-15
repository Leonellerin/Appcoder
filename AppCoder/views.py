from django.shortcuts import render



def inicio(request):
    return render(request, 'templates/AppCoder/index.html/')
