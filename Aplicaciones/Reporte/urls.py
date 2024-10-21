#configurando  redireccionamiento

from django.urls import path
from.import views

urlpatterns=[
    path('',views.home),
    path('listadoEmpresas/', views.listadoEmpresas, name='listadoEmpresas'),
    path('nuevaEmpresa/', views.nuevaEmpresa, name='nuevaEmpresa'),
   


]