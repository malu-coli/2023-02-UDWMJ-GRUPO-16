from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'animals'

router = routers.DefaultRouter()
router.register('animais', views.AnimalViewSet, basename='animais')

urlpatterns = [
    path('', views.list_animals, name='list_animals'),
    path('adicionar/', views.add_animal, name='add_animal'),
    path('editar/<int:id_animal>/', views.edit_animal, name='edit_animal'),
    path('excluir/<int:id_animal>/', views.delete_animal, name='delete_animal'),
]
