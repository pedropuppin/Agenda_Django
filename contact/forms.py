from . import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required = True,
        min_length = 2,  
    )
    
    last_name = forms.CharField(
        required = True,
        min_length = 2,  
    )
    
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já este e-mail!', code = 'invalid')
            )
        
        return email
