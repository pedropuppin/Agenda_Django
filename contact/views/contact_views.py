# esse arquivo só funciona dessa forma pq no __init__.py a gente tá importando 
# tudo que tem dentro dele

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request, 
        'contact/index.html',
    )
