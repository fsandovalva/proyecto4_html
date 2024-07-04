from django.urls import path
from .views import SerieListView, SerieDetailView, CapituloListView, CapituloDetailView, CapituloCreateView, SerieCreateView, CapituloDeleteView, SerieDeleteView, SerieUpdateView, CapituloUpdateView

app_name = 'series'

urlpatterns = [
    path('', SerieListView.as_view(), name='serie-list'),
    path('create/', SerieCreateView.as_view(), name='serie-create'),
    path('<int:pk>/', SerieDetailView.as_view(), name='serie-detail'),
    path('<int:pk>/editar/', SerieUpdateView.as_view(), name='serie-edit'),
    path('<int:pk>/delete/', SerieDeleteView.as_view(), name='serie-delete'),
    path('capitulos/', CapituloListView.as_view(), name='capitulo-list'),
    path('<int:serie_id>/capitulo/create/', CapituloCreateView.as_view(), name='capitulo-create'),
    path('capitulos/<int:pk>/', CapituloDetailView.as_view(), name='capitulo-detail'),
    path('capitulos/<int:pk>/editar', CapituloUpdateView.as_view(), name='capitulo-edit'),
    path('<int:serie_id>/capitulos/<int:pk>/delete/', CapituloDeleteView.as_view(), name='capitulo-delete'),
]