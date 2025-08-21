"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Adicione estas importações para servir arquivos de mídia em desenvolvimento (Aula 10)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('site-admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('site/', include('site_loja.urls', namespace='site_loja')),
    # URLs para autenticação - aula 10
    path('accounts/', include('django.contrib.auth.urls')), 
]

# Configuração para servir arquivos de mídia apenas em modo de desenvolvimento (Aula 10)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)