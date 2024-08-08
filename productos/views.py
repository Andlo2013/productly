from django.http import Http404, HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render

from .forms import ProductoForm
from .models import Producto

# Create your views here.

##filter items with stock >= <value>
#Productos=Producto.objects.filter(stock__gte=5)
##filter items with stock <= <value>
#Productos=Producto.objects.filter(stock__lte=5)
def index(request):
    ##Get all items
    productos=Producto.objects.all()
    print(productos)
    return render(request,'index.html',{'productos':productos}) 

    #Por defecto solo serializa diccionarios, por eso usamos safe=False
    #Es neceario convertir el queryset a una lista
    #return JsonResponse(list(productos),safe=False)


##filter by Id
#Productos=Producto.objects.get(id=1)
##Filter by primary-key
#Productos=Producto.objects.get(pk=1)
def detail(request,id):
    
    productoDb=get_object_or_404(Producto,id=id)

    return render(
        request,
        'detalle.html',
        {'producto':productoDb})

def formulario(request):
    if(request.method=='POST'):
        #Validar formulario
        form=ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    #En cas la petición NO es POST, se crea un formulario en blanco
    else:
        form=ProductoForm()
    return render(
        request,
        'producto_form.html',
        {'form':form})