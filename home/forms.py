# forms.py
from django import forms


class ContatoForm(forms.Form):
    
    nome = forms.CharField(
        max_length=100,
        label= "nome completo",
        widget=forms.TextInput(attrs={'class': 'form.control', 'placeholder': 'nome completo'})
        )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'})
    )

    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows':4})
    )




class ProdutoForm(forms.Form):

    nome = forms.CharField(max_length=100, 
                           label='Nome do Produto',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'})
                           )
    preco = forms.DecimalField(max_digits=10, 
                               decimal_places=2, 
                               label='Preço',
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor do produto'})
                               )

