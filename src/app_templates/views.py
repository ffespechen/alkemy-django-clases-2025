from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Articulo

# Create your views here.
def primer_template(request):
    return render(request, 'app_templates/template1.html')


def bootstap_template(request):
    return render(request, 'base.html')


def vista_heredero1(request, titulo, contenido):
    
    return render(request, 
                  'app_templates/heredero1.html',
                  {'var_titulo': titulo, 'var_contenido': contenido})

def listar_articulos(request):
    articulos = Articulo.objects.all()        

    return render(request,
                  'app_templates/listar.html', 
                  {'articulos': articulos})


def detalle_articulo(request, id):
    # articulo = Articulo.objects.get(id=id)
    articulo = get_object_or_404(Articulo, id=id)

    return render(request,
                  'app_templates/detalle.html',
                  {'articulo': articulo})


def listar_json(request):
    articulos = get_list_or_404(Articulo)
    articulos_json = serializers.serialize('json', articulos)
    return JsonResponse(articulos_json, safe=False)


def borrar_articulo(request, id):
    articulo_a_borrar = get_object_or_404(Articulo, id=id)
    articulo_a_borrar.delete() 
    return HttpResponseRedirect(reverse('app_templates:listar'))


def modificar_promocion(request, id):
    articulo_a_modificar = get_object_or_404(Articulo, id=id)
    articulo_a_modificar.promocion = not articulo_a_modificar.promocion
    articulo_a_modificar.save()
    return HttpResponseRedirect(reverse('app_templates:listar'))


class ArticuloCreateView(CreateView):
    model = Articulo 
    fields = '__all__'
    template_name = 'crear.html'
    success_url = reverse_lazy('app_templates:listar')


class ArticuloUpdateView(UpdateView):
    model = Articulo 
    fields = '__all__'
    template_name = 'crear.html'
    success_url = reverse_lazy('app_templates:listar')
    