from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def login(request):
    return render(request,'core/login.html')

def registro(request):
    return render(request,'core/registro.html')