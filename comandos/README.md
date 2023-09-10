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
python manage.py makemigrations
python manage.py migrate

```

- Criando e modificando a senha de um super usuário Django
```
python manage.py createsuperuser
python manage.py changepassword USERNAME

```
