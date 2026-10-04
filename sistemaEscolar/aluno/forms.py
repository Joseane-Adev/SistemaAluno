from django import forms
import re
from .models import Cadastro

class  CadastroForms(forms.ModelForm):
    class Meta:
             model = Cadastro
             fields = '__all__'
             exclude = ['matricula'] # não mostra no formulario

    nome_aluno = forms.CharField(
            label = 'Nome do aluno(a)',
            required= True,
            max_length= 100,
            widget= forms.TextInput(
                attrs={
                        'placeholder': 'Nome do aluno(a)',
                }
            )
        )
    data_nascimento = forms.DateField(
            input_formats=['%d/%m/%Y', '%Y-%m-%d'],
            label= 'Data de nascimento',
            required= True,    
        
        )
        
    nacionalidade_aluno = forms.CharField(
            label= 'Nacionalidade',
            required= True,
            max_length= 30,
        )
    nome_mae = forms.CharField(
            label= 'Nome da mãe',
            max_length= 100,
            required= True,
        )
    numero_mae = forms.CharField(
            label= 'Numero da mãe',
            required= True,
            max_length= 20,
        )
    nome_pai = forms.CharField(
            label= 'Nome do pai',
            required= True,
            max_length= 100,
        )
    numero_pai = forms.CharField(
                label= 'Numero do pai',
                required= True,
                max_length= 20,
        )
    endereco = forms.CharField(
            label= 'Endereço',
            max_length= 100,
            required= True,
        )
    bairro = forms.CharField(
            label= 'Bairro',
            required= True,
            max_length= 100,
        )
    numero_casa = forms.CharField(
            label= 'Numero da casa',
            required= True,
            max_length= 20,
        )
    telefone_extra = forms.CharField(
            label='Telefone extra',
            max_length= 20,
            required= False
        )
    turma = forms.CharField(
            label= 'Turma',
            max_length= 30,
        )

    def clean(self):

        cleaned_data = super().clean()

        campos_letras = ['nome_aluno', 'nome_mae', 'nome_pai', 'endereco', 'nacionalidade_aluno', 'bairro']
        for campo in campos_letras:
            valor = cleaned_data.get(campo)
            if valor and not re.match(r'^[A-Za-zÀ-ÿ\s]+$', valor):
                self.add_error(campo, 'Digite apenas letras!')

        #para telefone
        numeros = ['numero_mae', 'numero_pai']
        for campo in numeros:
            valor = cleaned_data.get(campo)
            if valor and not re.match(r'^\d{9,11}$', valor):
                self.add_error(campo, 'Só pode ter 9 digitos e 11!')
        
        return cleaned_data

