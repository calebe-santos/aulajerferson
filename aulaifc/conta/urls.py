from django.urls import path
from . import views

urlpatterns = [
    path('registar/', views.registrar, name='registrar'),
    path('minhha-conta/', views.minha_conta, name='minhaconta'),
    path('excluir-conta/', views.excluir_conta, name='excluir_conta'),
]