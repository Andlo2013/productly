#Para usar formularios en django se debe instalar el paquete django-forms (Productly/settings.py)
#Para crear un formulario se debe importar ModelForm
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
    class Meta:
        #El modelo que debe usar la clase
        model=Producto
        #Los campos que se deben mostrar en el formulario
        fields=['nombre','stock','puntaje','categoria']