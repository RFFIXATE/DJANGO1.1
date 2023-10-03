from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Favoritos
#from .forms import FavoritoForm
from .forms import FavoritoModelForm

# Create your views here.
def index_favoritos(request):
    favoritos_lista = Favoritos.objects.all()
    
    #for fav in favoritos_lista:
    #    print(fav.nombre)
    #    print(fav.url)

    context = {
        'favoritos_lista':favoritos_lista
    }


    return render(request, 'favoritos/lista.html', context)

def crear_favoritos(request):

     # form = FavoritoForm()
    form = FavoritoModelForm()

    if request.method == 'POST':
        form = FavoritoModelForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        
        
        
        #print(request.POST)
        #nombre = request.POST['nombre']
        #url = request.POST['url']
       # form = FavoritoForm(request.POST)
        #if form.is_valid():
       #     nombre = form.cleaned_data['nombre']
       #     url = form.cleaned_data['url']
      #      Favoritos.objects.create(nombre=nombre, url=url)
       # else:
       #     print(form.errors)
        #favorito = Favoritos()
        #favorito.nombre = nombre
        #favorito.url = url
        #favorito.save()

    context = {
        'form':form,
        'titulo':'Crear favorito'
    }
    return render(request, 'favoritos/crear.html', context)



def borrar_favoritos(request, pk):
    Favoritos.objects.get(pk=pk).delete()
    return redirect('favoritos:index')
    #return redirect(reverse('favoritos:borrar', kwargs={'pk':pk}))


def detalle_favoritos(request, pk):
    favorito = Favoritos.objects.get(pk=pk)
    return render(request,'favoritos/detalle.html', context={'object':favorito})


def actualizar_favoritos(request, pk):
    favorito = Favoritos.objects.get(pk=pk)
    # form = FavoritoForm()
    form = FavoritoModelForm(instance=favorito)

    if request.method == 'POST':
        form = FavoritoModelForm(request.POST, instance=favorito)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        
        #print(request.POST)
        #nombre = request.POST['nombre']
        #url = request.POST['url']
       # form = FavoritoForm(request.POST)
        #if form.is_valid():
       #     nombre = form.cleaned_data['nombre']
       #     url = form.cleaned_data['url']
      #      Favoritos.objects.create(nombre=nombre, url=url)
       # else:
       #     print(form.errors)
        #favorito = Favoritos()
        #favorito.nombre = nombre
        #favorito.url = url
        #favorito.save()

    context = {
        'form':form,
        'titulo':'Actualizar favorito'
    }
    return render(request, 'favoritos/crear.html', context)