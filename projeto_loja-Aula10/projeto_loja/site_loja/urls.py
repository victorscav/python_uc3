# projeto_loja/site_loja/urls.py

from django.urls import path
from . import views # Importa as views que acabamos de criar
from django.contrib.auth import views as auth_views

# Define o namespace para esta aplicação
app_name = 'site_loja' 

urlpatterns = [
    path('', views.home, name='home'), 
    #path('produtos/', views.lista_produtos, name='lista_produtos'), 
    path('produtos/', views.produtos_lista, name='produtos_lista'),
    path('perfil/', views.perfil, name='perfil'), # URL para a página de perfil
    path('login/', auth_views.LoginView.as_view(template_name='site_loja/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='site/'), name='logout'), # Redireciona para a home após o logout (Aula 11.01.02)
]