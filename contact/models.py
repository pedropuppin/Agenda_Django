from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    
class Contact(models.Model):
    # o id é gerado automaticamente pelo Django
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) # permite o campo ser opcional
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    
    # o Django executa a função quando for criado o contato
    created_date = models.DateTimeField(default=timezone.now)
    
    # não tem limitação de chars 
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    
    # cria uma chave estrangeira para o model Category
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True,
    )
    
    # consegue manipular o nome do contato na tela da área administrativa
    def __str__(self) -> str:
        return f'{self.first_name} - {self.email}'




# sempre que uma alteração é feita em um model eu tenho que rodar uma migração
# python manage.py makemigrations
