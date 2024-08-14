from django.urls import path
from . import views

urlpatterns = [
path('loginCSL/', views.loginCSL, name='login-CSL'),
path('CSL/', views.CSL, name='CSL'),
path('cadastrarveiculos/', views.cadastrarveiculos, name='cadastrar_veículos'),
path('cadastrousuarios/', views.cadastrousuarios, name='cadastro_usuários'),
path('autorizarveiculos/', views.autorizarveiculos, name='autorizar_veiculos'),
path('registros/', views.registros, name='registros_csl'),
path('excluircsl/', views.excluircsl, name='excluir_csl'),

]