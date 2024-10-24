from django.contrib import admin
from.models import Empresa,Usuario,Empleado,Encargado,Certificado


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Empleado)
admin.site.register(Encargado)
admin.site.register(Certificado)
