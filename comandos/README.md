- Iniciar projeto Django
```
# iniciar venv
python -m venv venv

# ativar venv
source venv/bin/activate

# instalar o django no venv
pip install django

# iniciar projeto
django-admin startproject project_name .

# crie um app novo e já adicione ele lá no INSTALED_APPS
python manage.py startapp nome_do_app

```

- Iniciar git repo
```
# configure o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore

# suba para o github
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
git branch -M main
git push -u origin main
```

```
Configurar os arquivos estáticos e os templates globai e colocar eles no settings.py

STATICFILES_DIRS = (
    BASE_DIR / 'base_static',
)

#No TEMPLATES
'DIRS': [
    BASE_DIR / 'base_templates'
],

```


- Migrando a base de dados do Django
```
# cria os arquivos de migração
python manage.py makemigrations

# faz a migração
python manage.py migrate

```

- Criando e modificando a senha de um super usuário Django
```
python manage.py createsuperuser
python manage.py changepassword USERNAME

```

```python

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')

```
