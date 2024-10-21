#configurando  redireccionamiento

from django.urls import path
from.import views

urlpatterns=[
    path('',views.home),
    path('listadoEmpresa/', views.listadoEmpresa, name='listadoEmpresa'),
   


]