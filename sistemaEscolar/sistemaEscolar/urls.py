"""
URL configuration for sistemaEscolar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from aluno import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path("admin/", admin.site.urls),
    path('', views.resposta , name = 'main'),#caminho da página
    path('cadastro/', views.cadastro , name='cadastro'),
    path('pesquisar/', views.pesquisar_alunos, name= 'pesquisar' ),
    path( 'ficha_aluno/<int:pk>/', views.ficha_aluno, name = 'ficha_aluno'),
    path('ficha_aluno/<int:pk>/pdf/', views.ficha_pdf, name= 'ficha_pdf'),
    path('logout', views.logout, name='logout')
]
