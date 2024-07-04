from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Reseña, Capitulo, Serie
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReseñaForm
from django.http import JsonResponse


def index(request):
    return render(request, 'series/index.html')
class ReseñaListView(ListView):
    model = Reseña
    template_name = 'reseñas/reseña_list.html'

class ReseñaDetailView(DetailView):
    model = Reseña
    template_name = 'reseñas/reseña_detail.html'

class ReseñaCreateView(LoginRequiredMixin, CreateView):
    model = Reseña
    form_class = ReseñaForm
    template_name = 'reseñas/reseña_form.html'
    success_url = reverse_lazy('reseñas:reseña-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

def obtener_episodios(request):
    serie_id = request.GET.get('serie_id')
    if serie_id:
        capitulos = Capitulo.objects.filter(serie_id=serie_id).values('id', 'titulo')
        episodios_list = list(capitulos)
        return JsonResponse(episodios_list, safe=False)
    return JsonResponse({'error': 'No serie_id provided'}, status=400)

class ReseñaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reseña
    template_name = 'reseñas/reseña_delete.html'
    success_url = reverse_lazy('series:serie-list')

class ReseñaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reseña
    fields = ['titulo', 'contenido', 'puntuacion', 'capitulo']
    template_name = 'reseñas/reseña_form.html'
    success_url = reverse_lazy('series:serie-list')