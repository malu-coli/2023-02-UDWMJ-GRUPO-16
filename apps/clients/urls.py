from django.urls import path
from . import views
from rest_framework import routers

app_name = 'clients'

router = routers.DefaultRouter()
router.register('clientes', views.ClientViewSet, basename='clientes')

urlpatterns = [
    path('', views.list_clients, name='list_clients'),
    path('adicionar/', views.add_client, name='add_client'),
    path('editar/<int:id_client>/', views.edit_client, name='edit_client'),
    path('excluir/<int:id_client>/', views.delete_client, name='delete_client'),
]
