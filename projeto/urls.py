from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('chamados.urls')),
    path('admin/', admin.site.urls),
    path('gerenciamento/',include('usuarios.urls')),
    path('gerenciamento/login',include('usuarios.urls')),
    path('gerenciamento/cadastro',include('usuarios.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
