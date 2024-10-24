#configurando  redireccionamiento

from django.urls import path
from.import views

urlpatterns=[
    
     path('', views.login_view, name='login'),
    path('home/', views.home, name='home'), 
    path('listadoEmpresas/', views.listadoEmpresas, name='listadoEmpresas'),
    path('nuevaEmpresa/', views.nuevaEmpresa, name='nuevaEmpresa'),
    path('guardarEmpresa/', views.guardarEmpresa),
    path('eliminarEmpresa/<id>', views.eliminarEmpresa),
    path('editarEmpresa/<id>', views.editarEmpresa),
    path('procesarActualizacionEmpresa/', views.procesarActualizacionEmpresa, name='procesarActualizacionEmpresa'),

#-----------------------------------------------------------------------------------------------------------------
    path('listadoEmpleados/', views.listadoEmpleado, name='listadoEmpleados'),
    path('eliminarEmpleado/<id>/', views.eliminarEmpleado, name='eliminarEmpleado'),
    path('nuevoEmpleado/', views.nuevoEmpleado, name='nuevoEmpleado'),
    path('guardarEmpleado/', views.guardarEmpleado, name='guardarEmpleado'),
    path('editarEmpleado/<id>/', views.editarEmpleado, name='editarEmpleado'),
    path('procesarActualizacionEmpleado/', views.procesarActualizacionEmpleado, name='procesarActualizacionEmpleado'),

#-----------------------------------------------------------------------------------------------------------------
    path('listadoEncargados/', views.listadoEncargado, name='listadoEncargados'),
    path('eliminarEncargado/<id>/', views.eliminarEncargado, name='eliminarEncargado'),
    path('nuevoEncargado/', views.nuevoEncargado, name='nuevoEncargado'),
    path('guardarEncargado/', views.guardarEncargado, name='guardarEncargado'),
    path('editarEncargado/<id>/', views.editarEncargado, name='editarEncargado'),
    path('procesarActualizacionEncargado/', views.procesarActualizacionEncargado, name='procesarActualizacionEncargado'),

#-----------------------------------------------------------------------------------------------------------------
    path('listadoCertificado/', views.listadoCertificado, name='listadoCertificado'),
    path('nuevoCertificado/', views.nuevoCertificado, name='nuevoCertificado'),
    path('guardarCertificado/', views.guardarCertificado, name='guardarCertificado'),
    path('editarCertificado/<id>/', views.editarCertificado, name='editarCertificado'),
    path('procesarActualizacionCertificado/', views.procesarActualizacionCertificado, name='procesarActualizacionCertificado'),
    path('eliminarCertificado/<id>/', views.eliminarCertificado, name='eliminarCertificado'),
    path('certificado/<int:certificado_id>/', views.generar_certificado, name='generar_certificado'),

]
