# O dunder init no nome do arquivo, indica pro python que isso é um pacote python.
# E também fala que quando vc importar esse pacote, esse arquivo é a primeira coisa a ser 
# executada.

# criamos a pasta views para simular que o views.py é esse arquivo.
# ajuda a organizar o app se começar a ter muitas views.

from .contact_views import *
from .contact_forms import *
from .user_forms import *
