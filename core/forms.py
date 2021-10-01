from django import forms

from core import models

class ContatoForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = [
            'nome',
            'telefone',
            'celular',
            'email',
            'endereco'
        ]
