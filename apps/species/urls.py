from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'species'

router = routers.DefaultRouter()
router.register('especies', views.SpecieViewSet, basename='especie')

urlpatterns = [
    path('', include(router.urls) )
]