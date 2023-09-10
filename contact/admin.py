from django.contrib import admin
from contact import models

# Register your models here.

# é uma configuração do seu model na admin do django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name','phone',
    ordering = '-id', # ordena os registros do maior para o menor
    # list_filter = 'created_date', # filtra os registros por data de criação'
    search_fields = 'id', 'first_name', 'last_name', # adiciona um campo de pesquisa 
    list_per_page = 10 # exibe 10 registros por página
    list_max_show_all = 100
    # list_editable = 'phone', # permite editar direto no admin

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
