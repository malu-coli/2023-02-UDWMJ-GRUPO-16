from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'breeds'

router = routers.DefaultRouter()
router.register('racas', views.BreedViewSet, basename='racas')

urlpatterns = [
    path('', views.list_breeds, name='list_breeds'),
    path('adicionar/', views.add_breed, name='add_breed'),
    path('editar/<int:id_breed>/', views.edit_breed, name='edit_breed'),
    path('excluir/<int:id_breed>/', views.delete_breed, name='delete_breed'),
]