from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'breeds'

router = routers.DefaultRouter()
router.register('racas', views.BreedViewSet, basename='racas')

urlpatterns = [
    path('', include(router.urls) )
]