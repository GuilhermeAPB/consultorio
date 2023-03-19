from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm
from django.shortcuts import get_object_or_404


# Precisamos criar as visualizações do nosso site. As visualizações definem como as informações serão exibidas na página web.

# Este código define quatro visualizações: paciente_list, paciente_create, paciente_update e paciente_delete.
# A visualização paciente_list lista todos os pacientes registrados no banco de dados.
# A visualização paciente_create exibe um formulário para adicionar um novo paciente.
# A visualização paciente_update exibe um formulário para atualizar as informações de um paciente existente.
# A visualização paciente_delete exibe uma tela de confirmação antes de excluir um paciente.

# O código define quatro funções de visualização:
# paciente_list: recupera todos os pacientes do banco de dados e renderiza o template paciente_list.html com a lista de pacientes.
# paciente_create: exibe um formulário para adicionar um novo paciente ou salva o formulário enviado pelo usuário.
# paciente_update: exibe um formulário pré-preenchido com as informações do paciente a ser atualizado ou salva o formulário enviado pelo usuário.
# paciente_delete: exibe uma tela de confirmação antes de excluir o paciente ou exclui o paciente se o formulário for enviado pelo usuário.


def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente_list.html', {'pacientes': pacientes})


def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'paciente_form.html', {'form': form})


def paciente_update(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'paciente_form.html', {'form': form})


def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_list')
    return render(request, 'paciente_confirm_delete.html', {'paciente': paciente})
