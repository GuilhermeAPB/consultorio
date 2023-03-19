from django.db import models

# precisamos criar nossos modelos de banco de dados. Os modelos definem como as informações do nosso site serão armazenadas no banco de dados.
# Este código define um modelo Paciente com vários campos, como nome, email, telefone, data_nascimento e queixa.
# Também definimos um campo created_at que será automaticamente preenchido com a data e hora em que o registro foi criado.


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    queixa = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
