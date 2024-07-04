from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Serie, Capitulo
from django.urls import reverse, reverse_lazy
from .forms import CapituloForm
from apps.reseñas.models import Reseña
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class SerieListView(ListView):
    model = Serie
    template_name = 'series/serie_list.html'

class SerieDetailView(DetailView):
    model = Serie
    template_name = 'series/serie_detail.html'
    context_object_name = 'serie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['capitulos'] = self.object.capitulos.all()
        context['reseñas'] = Reseña.objects.filter(serie=self.object)
        return context

class SerieCreateView(LoginRequiredMixin, CreateView):
    model = Serie
    template_name = 'series/serie_form.html'
    fields = ['titulo', 'sinopsis','imagen']
    success_url = reverse_lazy('series:serie-list')
    
    def form_valid(self, form):
        if self.request.FILES:
            form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)
    
class SerieUpdateView(LoginRequiredMixin, UpdateView):
    model = Serie
    fields = ['titulo', 'sinopsis','imagen']
    template_name = 'series/serie_form.html'
    success_url = reverse_lazy('series:serie-list')
    
    def form_valid(self, form):
        if self.request.FILES:
            form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)
    
class SerieDeleteView(LoginRequiredMixin, DeleteView):
    model = Serie
    template_name = 'series/serie_delete.html'
    success_url = reverse_lazy('series:serie-list')

class CapituloListView(ListView):
    model = Capitulo
    template_name = 'series/capitulo_list.html'

class CapituloDetailView(DetailView):
    model = Capitulo
    template_name = 'series/capitulo_detail.html'

class CapituloCreateView(LoginRequiredMixin, CreateView):
    model = Capitulo
    form_class = CapituloForm
    template_name = 'series/capitulo_form.html'
    
    def form_valid(self, form):
        # Obtener la serie a partir del parámetro en la URL
        serie_id = self.kwargs['serie_id']
        serie = get_object_or_404(Serie, id=serie_id)
        # Asignar la serie al capítulo que se está creando
        form.instance.serie = serie
        return super().form_valid(form)
    
    def get_success_url(self):
        # Redirigir a la página de detalle de la serie después de crear el capítulo
        return reverse('series:serie-detail', kwargs={'pk': self.kwargs['serie_id']})

class CapituloUpdateView(LoginRequiredMixin, UpdateView):
    model = Capitulo
    form_class = CapituloForm
    template_name = 'series/capitulo_form.html'
    
    def get_success_url(self):
        # Redirigir a la página de detalle de la serie después de actualizar el capítulo
        return reverse('series:serie-detail', kwargs={'pk': self.object.serie.pk})

class CapituloDeleteView(LoginRequiredMixin, DeleteView):
    model = Capitulo
    template_name = 'series/capitulo_delete.html'
    success_url = reverse_lazy('series:serie-list')