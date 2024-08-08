from django.contrib import admin
from .models import Categoria, Producto

#Estas clases definen la informacion que se mostrara en el panel de administracion
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','stock','creado_en')
    search_fields = ('nombre', 'categoriaId__nombre')
    #Indica que campos no queremos que aparezcan en los formularios
    #Como tenemos solo un campo, dejamos una coma al final para que django sepa que es una tupla
    exclude = ('creado_en',)
    #Indica que campos queremos que aparezcan en los formularios
    #fields = ('nombre','stock','puntaje','categoriaId')



# Register your models here.
#Esto hace que nuestros modelos sean visibles en el panel de administracion
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
