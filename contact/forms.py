from . import models
from django import forms
from django.core.exceptions import ValidationError

# criando um formulário a partir de um modelo(forms.ModelForm)
class ContactForm(forms.ModelForm):
    # os widgets são os elementos que serão renderizados na tela
    first_name = forms.CharField(
        widget = forms.TextInput(
            # attrs são os atributos do elemento
            attrs = {
                'class': 'minha-nova-classe',
                'placeholder': 'Digite seu nome',
            }
        ),
        label = 'Nome',
        # help_text = 'Digite seu nome',
    )
    
    picture = forms.ImageField( # cria o campo novamente
        widget = forms.FileInput( # fala que é pra ser um campo de arquivo
            attrs = {
                'accept': 'image/*', # aceita qualquer imagem que for enviada
            } 
        )
    )
    
    class Meta:
        model = models.Contact # informa qual o model em que o form é baseado
        fields = ( # informa quais campos serão utilizados no formulário
            'first_name', 
            'last_name', 
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )
        
    # uma forma de validar campos para quando vc precisa de mais de uma validação de campos diferentes
    def clean(self):
        # todos os dados vem de self.cleaned_data
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao sobrenome',
                code='invalid'
            )
            
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
                
        return super().clean()


    # Outra forma de falidação de um campo expecífico
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'João':
            self.add_error(
                'First_name',
                ValidationError(
                    'João não pode',
                    code='invalid'
                )
            )
            
        return first_name
