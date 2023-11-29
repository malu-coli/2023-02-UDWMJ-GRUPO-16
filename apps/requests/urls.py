from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'requests'

router = routers.DefaultRouter()
router.register('solicitacoes', views.RequestViewSet, basename='solicitacoes')

urlpatterns = [
    path('', include(router.urls) )
]
