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
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from django.conf import settings
import os
import locale


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

            messages.success(request, 'Empresa actualizado con éxito')
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


def guardarCertificado(request):
    if request.method == 'POST':
        encargado_id = request.POST.get("encargado")  # Sin la coma
        empleado_id = request.POST.get("empleado")

        # Asegúrate de que estás pasando IDs válidos como enteros
        nuevoCertificado = Certificado.objects.create(
            encargado_id=int(encargado_id),
            empleado_id=int(empleado_id)
        )

        messages.success(request, "Certificado registrado exitosamente")
        return redirect('listadoCertificado')

    # Otras acciones en caso de que no sea POST
    return render(request, 'listadocertificado.html')

# Renderizando formulario de actualización de encargado
def editarCertificado(request, id): 
    certificadoEditar = Certificado.objects.get(id=id)
    encargadosBdd = Encargado.objects.all()
    empleadosBdd = Empleado.objects.all()    
    return render(request, 'editarcertificado.html', {'certificadoEditar': certificadoEditar, 'encargados': encargadosBdd, 'empleados': empleadosBdd})  


def procesarActualizacionCertificado(request):
    if request.method == 'POST':
        id_certificado = request.POST['id']
        encargado_id = request.POST.get("encargado")
        empleado_id = request.POST.get("empleado")

        try:
            # Obtener el certificado que se va a actualizar
            certificadoConsultado = Certificado.objects.get(id=id_certificado)

            # Actualizar los campos correctamente (sin coma)
            certificadoConsultado.encargado_id = int(encargado_id)
            certificadoConsultado.empleado_id = int(empleado_id)

            # Guardar los cambios
            certificadoConsultado.save()

            # Mensaje de éxito
            messages.success(request, 'Certificado actualizado con éxito')
        except Certificado.DoesNotExist:
            messages.error(request, 'El certificado no existe')

    return redirect('listadoCertificado')
#-----------------------------------------------ELIMINAR CERTIFICADO--------------------------------------------------------------------------
# Eliminar encargado
def eliminarCertificado(request, id):
    certificadoEliminar = Certificado.objects.get(id=id)
    certificadoEliminar.delete()
    messages.success(request, "Certificado eliminado exitosamente")
    return redirect('listadoCertificado')

#---------------------------------------------------certificado PDF--------------------------------------------------------------------
def generar_certificado(request, certificado_id):
    try:
        certificado = Certificado.objects.get(id=certificado_id)
    except Certificado.DoesNotExist:
        return HttpResponse("Certificado no encontrado", status=404)

    # Configurar la respuesta HTTP para el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificado_{certificado.id}.pdf"'

    # Crear el canvas para el PDF con tamaño carta
    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica-Bold", 14)

    # Obtener datos del empleado y encargado
    empleado = certificado.empleado
    encargado = certificado.encargado
    # Establecer la localización a español
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime('%d de %B del %Y')

    # Dibujar el logo de la empresa (izquierda)
    if encargado.empresa.logo:
        p.drawImage(encargado.empresa.logo.path, 50, 700, width=100, height=100, preserveAspectRatio=True)

    # Dibujar la descripción de la empresa (a la derecha del logo)
    p.setFont("Helvetica", 10)
    text_desc = p.beginText(350, 750)  # Ajustar la posición para alinear con el logo
    text_desc.textLine("DESARROLLO DE SISTEMAS - CAPACITACIÓN")
    text_desc.textLine("PÁGINAS WEB - APLICACIONES MÓVILES")
    text_desc.textLine("CONSULTORÍA & SEGURIDAD INFORMÁTICA")
    text_desc.textLine("INTELIGENCIA DE NEGOCIO – INFRAESTRUCTURA ")
    text_desc.textLine("                                TECNOLÓGICA")
    p.drawText(text_desc)

   # Agregar el título del certificado en negrita y subrayado
    titulo = "CERTIFICADO DE HONORABILIDAD"
    p.setFont("Helvetica-Bold", 14)  # Aumentar ligeramente la fuente para énfasis
    x_titulo = 200
    y_titulo = 620

    p.drawString(x_titulo, y_titulo, titulo)  # Dibujar el título
    p.setLineWidth(1)  # Definir grosor de la línea
    p.line(x_titulo, y_titulo - 2, x_titulo + p.stringWidth(titulo, "Helvetica-Bold", 14), y_titulo - 2)  # Dibujar subrayado

    # Configuración del contenido del certificado (centrado debajo del logo y la descripción)
    p.setFont("Helvetica", 12)
    text = p.beginText(100, 580)
    text.textLine(f"Quito, {fecha_actual}")
    # Convertir nombres y apellidos del encargado a mayúsculas
    encargado_nombre_completo = f"{encargado.nombres.upper()} {encargado.apellido_paterno.upper()} {encargado.apellido_materno.upper()}"
    text.textLine("")
    text.textLine(
        f"Yo, {encargado_nombre_completo}, director de tecnologías de {encargado.empresa.nombre},"
        
    )
    text.textLine(f"con RUC {encargado.empresa.ruc}, a quien corresponda y a petición verbal de la interesada:")
    text.textLine("")
    text.textLine("CERTIFICO CONOCER:")
    text.textLine("")
    empleado_nombre_completo = f"{empleado.nombres.upper()} {empleado.apellido_paterno.upper()} {empleado.apellido_materno.upper()}"

    text.textLine(f" A {empleado_nombre_completo},con cédula de ciudadanía {empleado.cedula}, por un lapso")
    text.textLine(" de 5 años tiempo en el cual ha demostrado ser una persona respetuosa, seria, responsable,")
    text.textLine("trabajadora y honrada, la cual se ha ganado mi aprecio y consideración.")  
    text.textLine("")
    text.textLine("Es todo lo que puedo decir en honor a la verdad, facultándole a la interesada el uso del")
    text.textLine("presente certificado como lo creyere conveniente.")
    text.textLine("")
    text.textLine("")
  
    text.textLine("Atentamente,")
    text.textLine("")
    text.textLine("--------------------------------------------------")
    

 
    
    text.textLine(f"{encargado.nombres} {encargado.apellido_paterno} {encargado.apellido_materno}")
    text.textLine(f"{encargado.cargo}")
    text.textLine(f"Cédula: {encargado.cedula}")
    text.textLine(f"Celular: {encargado.telefono}")
    text.textLine(f"Email: {encargado.email}")
    # Logo de la empresa
    logo_path = os.path.join(settings.STATICFILES_DIRS[0], 'images/logo1.jpeg')  # Asegúrate de que la imagen esté en 'static/images'
    p.drawImage(logo_path, 400, 320, width=150, height=100, preserveAspectRatio=True)
    

    # Agregar el texto al PDF
    p.drawText(text)

    # Guardar y cerrar el PDF
    p.showPage()
    p.save()

    return response