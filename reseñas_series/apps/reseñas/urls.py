from django.urls import path
from .views import ReseñaListView, ReseñaDetailView, ReseñaCreateView, obtener_episodios, ReseñaDeleteView, ReseñaUpdateView

app_name = 'reseñas'

urlpatterns = [
    path('', ReseñaListView.as_view(), name='reseña-list'),
    path('<int:pk>/', ReseñaDetailView.as_view(), name='reseña-detail'),
    path('create/', ReseñaCreateView.as_view(), name='reseña-create'),
    path('obtener_episodios/', obtener_episodios, name='obtener_episodios'), 
    path('<int:pk>/delete/', ReseñaDeleteView.as_view(), name='reseña-delete'),
    path('<int:pk>/editar/', ReseñaUpdateView.as_view(), name='reseña-edit'),
]