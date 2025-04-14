from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Relacionado

# Create your views here.
class RelacionadoListView(ListView):
    # model = Relacionado
    queryset = Relacionado.objects.all()
    template_name = 'app_relacionada/listar.html'
    context_object_name = 'lista_relacionados'


class RelacionadoCreateView(CreateView):
    model = Relacionado 
    fields = ['articulo', 'leyenda', 'fecha']
    success_url = reverse_lazy('app_relacionada:listar')
    template_name = 'crear.html'


class RelacionadoUpdateView(UpdateView):
    model = Relacionado 
    fields = '__all__'
    success_url = reverse_lazy('app_relacionada:listar')
    template_name = 'crear.html'


class RelacionadoDeleteView(DeleteView):
    model = Relacionado
    template_name = 'app_relacionada/borrar.html'
    success_url = reverse_lazy('app_relacionada:listar')
    

def relacionado_detalle(request, pk):
    relacionado = get_object_or_404(Relacionado, pk=pk)
    return render(request,
                  'app_relacionada/detalle.html', 
                  {'relacionado': relacionado})