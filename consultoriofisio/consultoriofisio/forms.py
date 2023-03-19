from django import forms
from .models import Paciente

# Precisamos criar um formulário para adicionar e atualizar pacientes.

# Este código define um formulário baseado no modelo Paciente que criamos anteriormente.
# O formulário inclui campos para nome, email, telefone, data_nascimento e queixa.


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'telefone', 'data_nascimento', 'queixa']
