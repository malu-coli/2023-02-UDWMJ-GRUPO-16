from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('especies/', include('species.urls', namespace='species')),
    path('racas/', include('breeds.urls', namespace='breeds')),
]