#configurando  redireccionamiento

from django.urls import path
from.import views

urlpatterns=[
    path('',views.home),
    path('listadoEmpresas/', views.listadoEmpresas, name='listadoEmpresas'),
    path('nuevaEmpresa/', views.nuevaEmpresa, name='nuevaEmpresa'),
    path('guardarEmpresa/', views.guardarEmpresa),
    path('eliminarEmpresa/<id>', views.eliminarEmpresa),
    path('editarEmpresa/<id>', views.editarEmpresa),
    path('procesarActualizacionEmpresa/', views.procesarActualizacionEmpresa, name='procesarActualizacionEmpresa'),
]