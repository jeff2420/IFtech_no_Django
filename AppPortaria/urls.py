
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginPortaria/', views.loginPortaria, name='login-portaria'),
    path('portaria/', views.portaria, name='portaria'),
    path('registrar/', views.registrar_portaria, name='registrar'),
    path('registrosPortaria/', views.registrosPortaria, name='registros-portaria'),
    path('excluirPortaria/', views.excluirPortaria, name='excluir-portaria'),
    path('cadastrarVisitantes/', views.cadastrarVisitantes, name='cadastrar-visitantes'),

]
