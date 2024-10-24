from django.db import models

# Create your models here.
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=100)
    logo = models.FileField(upload_to='empresas', null=True, blank=True)

    def __str__(self):
            fila="{0}:{1} {2} {3}"
            return fila.format(self.id,self.ruc,self.nombre,self.descripcion)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Se recomienda almacenar contraseñas cifradas

    def __str__(self):
            fila="{0}:{1} {2}"
            return fila.format(self.id,self.username,self.password)

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    apellido_paterno = models.CharField(max_length=250)
    apellido_materno = models.CharField(max_length=250)
    nombres = models.CharField(max_length=250)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
            fila="{0}:{1} {2} {3} {4} {5} {6} {7}"
            return fila.format(self.id,self.cedula,self.apellido_paterno,self.apellido_paterno,self.nombres,self.direccion,self.telefono,self.email)


class Encargado(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    apellido_paterno = models.CharField(max_length=250)
    apellido_materno = models.CharField(max_length=250)
    nombres = models.CharField(max_length=250)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
            fila="{0}:{1} {2} {3} {4} {5} {6} {7}"
            return fila.format(self.id,self.cedula,self.apellido_paterno,self.apellido_paterno,self.nombres,self.cargo,self.telefono,self.email)


class Certificado(models.Model):
     id = models.AutoField(primary_key=True)
     empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True, blank=True)
     encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE,null=True, blank=True)
