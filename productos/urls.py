from django.urls import path
#Indica a python que se importe el archivo views de nuestra carpeta
#esto en caso de que alguna dependencia tenga el mismo nombre (Muy comun en este caso)
from . import views

#app_name es el nombre de la aplicacion
#Esto es una convencion de django, si encuentra esta variable agregara el nombre de la aplicacion
#al principio de la url, lo que evita conflictos entre urls de diferentes aplicaciones
app_name='productos'

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:id>',views.detail,name='detalle'),
    path('formulario',views.formulario,name='formulario'),
]