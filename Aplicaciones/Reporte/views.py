
from django.shortcuts import render, redirect
from .models import Empresa
from django.contrib import messages

# Create your views here.
# Create your views here.
def home(request):
    return render(request, "home.html")

# Insertando una nueva empresa en la base de datos
def guardarEmpresa(request):
    if request.method == 'POST':
        ruc = request.POST['ruc']
        nombre_empresa = request.POST['nombre_empresa']
        descripcion = request.POST['descripcion']

        nuevaEmpresa = Empresa.objects.create(
            ruc=ruc,
            nombre_empresa=nombre_empresa,
            descripcion=descripcion
        )

        messages.success(request, "Empresa registrada exitosamente")
        return redirect('listadoEmpresas')

# Listado de empresas
def listadoEmpresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'listadoEmpresa.html', {'empresas': empresas})

# Renderizando formulario para nueva empresa
def nuevaEmpresa(request):
    return render(request, 'nuevaEmpresa.html')
