from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.criar_usuario, name='criar_usuario'),
    path('consulta/', views.consulta_usuario, name='consulta_usuario'),
]