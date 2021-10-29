from django import forms
from django.forms.widgets import Textarea
from django.utils.regex_helper import Choice
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipo_de_classes

class PassagemForms(forms.Form):

    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa= forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipo_de_classes)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=100)