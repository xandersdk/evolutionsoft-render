from django.shortcuts import render,redirect
from datetime import datetime
from django.core.files.storage import default_storage
from django.db.models.deletion import ProtectedError
from .models import Empresa
from.models import Empleado
from.models import Encargado
from.models import Certificado
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
# Create your views here.
def home(request):
    return render(request, "home.html")

# Insertando una nueva empresa en la base de datos
def guardarEmpresa(request):
    if request.method == 'POST':
        ruc = request.POST['ruc']
        nombre = request.POST['nombre_empresa']
        descripcion = request.POST['descripcion']
        logo= request.FILES.get("foto")

        nuevaEmpresa = Empresa.objects.create(
            ruc=ruc,
            nombre=nombre,
            descripcion=descripcion,
            logo=logo
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

def eliminarEmpresa(request, id):
    empresaEliminar = Empresa.objects.get(id=id)
    empresaEliminar.delete()
    messages.success(request, 'Empresa eliminado exitosamente')
    return redirect('listadoEmpresas')

def editarEmpresa(request, id):
    empresaEditar = Empresa.objects.get(id=id)
    return render(request, 'editarempresa.html', {'empresaEditar': empresaEditar})

# Actualizando los nuevos datos en la base de datos
def procesarActualizacionEmpresa(request):
    if request.method == 'POST':
        id = request.POST['id']
        ruc = request.POST['ruc']
        nombre = request.POST['nombre_empresa']
        descripcion = request.POST['descripcion']
        logo= request.FILES.get("foto") # Obtener el archivo de la foto

        try:
            empresaConsultado = Empresa.objects.get(id=id)
            empresaConsultado.ruc = ruc
            empresaConsultado.nombre = nombre
            empresaConsultado.descripcion = descripcion

            if logo:
                empresaConsultado.logo = logo  # Actualizar la foto solo si se proporciona un nuevo archivo

            empresaConsultado.save()

            messages.success(request, 'Cliente actualizado con éxito')
        except Empresa.DoesNotExist:
            messages.error(request, 'El Cliente no existe')

    return redirect('listadoEmpresas')

#-------------------------Empleado------------------------------------------------------------------------------------------


# Renderizando el template de listado de empleados
def listadoEmpleado(request):
    empleadosBdd = Empleado.objects.all()
    empresasBdd = Empresa.objects.all()
    return render(request, 'listadoEmpleados.html', {'empleados': empleadosBdd, 'empresas':empresasBdd})


# Eliminar empleado
def eliminarEmpleado(request, id):
    empleadoEliminar = Empleado.objects.get(id=id)
    empleadoEliminar.delete()
    messages.success(request, "Empleado eliminado exitosamente")
    return redirect('listadoEmpleados')




# Renderizando formulario para nuevo empleado
def nuevoEmpleado(request):
    empresasBdd = Empresa.objects.all()
    return render(request, 'nuevoEmpleado.html', {'empresas':empresasBdd})


# Insertando empleado en la base de datos

def guardarEmpleado(request):
    if request.method == 'POST':
        cedula = request.POST["cedula"]
        apellido_paterno = request.POST["apellido_paterno"]
        apellido_materno = request.POST["apellido_materno"]
        nombres = request.POST["nombres"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        empresa_id = request.POST.get("empresa")  # Suponiendo que recibes el id de la empresa

        nuevoEmpleado = Empleado.objects.create(
            cedula=cedula,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            nombres=nombres,
            direccion=direccion,
            telefono=telefono,
            email=email,
            empresa_id=empresa_id  # Guardar el ID de la empresa
        )

        messages.success(request, "Empleado registrado exitosamente")
        return redirect('listadoEmpleados')

# Renderizando formulario de actualización de empleado
def editarEmpleado(request, id):
    empleadoEditar = Empleado.objects.get(id=id)
    empresasBdd = Empresa.objects.all()
    return render(request, 'editarEmpleado.html', {'empleadoEditar': empleadoEditar,'empresas':empresasBdd})

# Actualizando los nuevos datos en la base de datos
def procesarActualizacionEmpleado(request):
    if request.method == 'POST':
        id_empleado = request.POST['id']
        cedula = request.POST['cedula']
        apellido_paterno = request.POST['apellido_paterno']
        apellido_materno = request.POST['apellido_materno']
        nombres = request.POST['nombres']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        empresa_id = request.POST.get("empresa")  # Suponiendo que también recibes el id de la empresa

        try:
            empleadoConsultado = Empleado.objects.get(id=id_empleado)
            empleadoConsultado.cedula = cedula
            empleadoConsultado.apellido_paterno = apellido_paterno
            empleadoConsultado.apellido_materno = apellido_materno
            empleadoConsultado.nombres = nombres
            empleadoConsultado.direccion = direccion
            empleadoConsultado.telefono = telefono
            empleadoConsultado.email = email
            empleadoConsultado.empresa_id = empresa_id  # Actualizar la empresa

            empleadoConsultado.save()

            messages.success(request, 'Empleado actualizado con éxito')
        except Empleado.DoesNotExist:
            messages.error(request, 'El empleado no existe')

    return redirect('listadoEmpleados')
#-------------------------Encargado------------------------------------------------------------------------------------------
# Listado de encargados
def listadoEncargado(request):
    encargadosBdd = Encargado.objects.all()
    empresasBdd = Empresa.objects.all()
    return render(request, 'listadoEncargados.html', {'encargados': encargadosBdd, 'empresas': empresasBdd})


# Eliminar encargado
def eliminarEncargado(request, id):
    encargadoEliminar = Encargado.objects.get(id=id)
    encargadoEliminar.delete()
    messages.success(request, "Encargado eliminado exitosamente")
    return redirect('listadoEncargados')


# Renderizando formulario para nuevo encargado
def nuevoEncargado(request):
    empresasBdd = Empresa.objects.all()
    return render(request, 'nuevoEncargado.html', {'empresas': empresasBdd})


# Insertando encargado en la base de datos
def guardarEncargado(request):
    if request.method == 'POST':
        cedula = request.POST["cedula"]
        apellido_paterno = request.POST["apellido_paterno"]
        apellido_materno = request.POST["apellido_materno"]
        nombres = request.POST["nombres"]
        cargo = request.POST["cargo"]  # Nuevo campo "Cargo"
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        empresa_id = request.POST.get("empresa")  # Suponiendo que recibes el id de la empresa

        nuevoEncargado = Encargado.objects.create(
            cedula=cedula,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            nombres=nombres,
            cargo=cargo,  # Guardar el cargo del encargado
            telefono=telefono,
            email=email,
            empresa_id=empresa_id
        )

        messages.success(request, "Encargado registrado exitosamente")
        return redirect('listadoEncargados')


# Renderizando formulario de actualización de encargado
def editarEncargado(request, id):
    encargadoEditar = Encargado.objects.get(id=id)
    empresasBdd = Empresa.objects.all()
    return render(request, 'editarEncargado.html', {'encargadoEditar': encargadoEditar, 'empresas': empresasBdd})


# Actualizando los nuevos datos del encargado en la base de datos
def procesarActualizacionEncargado(request):
    if request.method == 'POST':
        id_encargado = request.POST['id']
        cedula = request.POST['cedula']
        apellido_paterno = request.POST['apellido_paterno']
        apellido_materno = request.POST['apellido_materno']
        nombres = request.POST['nombres']
        cargo = request.POST['cargo']  # Actualizar el campo "Cargo"
        telefono = request.POST['telefono']
        email = request.POST['email']
        empresa_id = request.POST.get("empresa")  # Suponiendo que también recibes el id de la empresa

        try:
            encargadoConsultado = Encargado.objects.get(id=id_encargado)
            encargadoConsultado.cedula = cedula
            encargadoConsultado.apellido_paterno = apellido_paterno
            encargadoConsultado.apellido_materno = apellido_materno
            encargadoConsultado.nombres = nombres
            encargadoConsultado.cargo = cargo  # Actualizar el cargo del encargado
            encargadoConsultado.telefono = telefono
            encargadoConsultado.email = email
            encargadoConsultado.empresa_id = empresa_id  # Actualizar la empresa

            encargadoConsultado.save()

            messages.success(request, 'Encargado actualizado con éxito')
        except Encargado.DoesNotExist:
            messages.error(request, 'El encargado no existe')

    return redirect('listadoEncargados')

#-------------------------Certificado------------------------------------------------------------------------------------------
def listadoCertificado(request):
    certificadosBdd = Certificado.objects.all()
    encargadosBdd = Encargado.objects.all()
    empleadosBdd = Empleado.objects.all()
    return render(request, 'listadocertificado.html', {'certificados':certificadosBdd,'encargados': encargadosBdd, 'empleados': empleadosBdd})


# Renderizando formulario para nuevo encargado
def nuevoCertificado(request):
    encargadosBdd = Encargado.objects.all()
    empleadosBdd = Empleado.objects.all()
    return render(request, 'nuevocertificado.html', {'encargados': encargadosBdd, 'empleados': empleadosBdd})