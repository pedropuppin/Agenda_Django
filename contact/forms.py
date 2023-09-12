from . import models
from django import forms
from django.core.exceptions import ValidationError

# criando um formulário a partir de um modelo
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite seu nome',
            }
        ),
        label = 'Nome',
        # help_text = 'Digite seu nome',
    )
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 
            'last_name', 
            'phone',
            'email',
            'description',
            'category',
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
