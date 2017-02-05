from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Categoria, Foto

# Create your views here.

def base(request):
    return render(request, 'base.html')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'album/categoria.html'

"""
def listar_categorias(request):
    lista_categorias = Categoria.objects.all()
    return render(request, 'album/categoria.html', {'object_list': lista_categorias})
"""

class CategoriaDetailView(DetailView):
    model = Categoria

"""
def detalle_categoria(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    return render(request, 'album/categoria_detail.html', {'object': categoria})
"""

class CategoriaCreate(CreateView):
    model = Categoria
    fields = '__all__'

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = '__all__'

class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('lista-categorias')

class FotoListView(ListView):
    model = Foto

class FotoDetailView(DetailView):
    model = Foto

class FotoCreate(CreateView):
    model = Foto
    fields = '__all__' # a list of the fields that you want to include in the form

class FotoUpdate(UpdateView):
    model = Foto
    fields = '__all__'

class FotoDelete(DeleteView):
    model = Foto
    success_url = reverse_lazy('lista-fotos')