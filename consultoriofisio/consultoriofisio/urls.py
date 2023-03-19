"""consultoriofisio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import paciente_list, paciente_create, paciente_update, paciente_delete


# O código acima define quatro URLs que mapeiam para as funções de visualização que criamos anteriormente.
# A URL raiz ('') mapeia para paciente_list, que exibe a lista de pacientes.
# A URL /create/ mapeia para paciente_create, que exibe o formulário para adicionar um novo paciente.
# As URLs <int:pk>/update/ e <int:pk>/delete/ mapeiam para as funções paciente_update e paciente_delete,
# respectivamente, que atualizam ou excluem um paciente específico.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paciente_list, name='paciente_list'),
    path('create/', paciente_create, name='paciente_create'),
    path('<int:pk>/update/', paciente_update, name='paciente_update'),
    path('<int:pk>/delete/', paciente_delete, name='paciente_delete'),
]
