from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'requests'

router = routers.DefaultRouter()
router.register('solicitacoes', views.RequestViewSet, basename='solicitacoes')

urlpatterns = [
    path('', views.list_requests, name='list_requests'),
    path('adicionar/', views.add_request, name='add_request'),
    path('editar/<int:id_request>/', views.edit_request, name='edit_request'),
    path('excluir/<int:id_request>/', views.delete_request, name='delete_request'),
    path('aceitar/<int:request_id>/', views.accept_request, name='accept_request'),
    path('recusar/<int:request_id>/', views.decline_request, name='decline_request'),
]