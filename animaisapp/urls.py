from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('especies/', include('species.urls', namespace='species')),
    path('racas/', include('breeds.urls', namespace='breeds')),
    path('animais/', include('animals.urls', namespace='animals')),
    path('clientes/', include('clients.urls', namespace= 'clients')),
    path('solicitacoes/', include('requests.urls', namespace= 'requests')),
    path('', include('core.urls', namespace='core')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)