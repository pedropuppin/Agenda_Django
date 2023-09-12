# esse arquivo só funciona dessa forma pq no __init__.py a gente tá importando 
# tudo que tem dentro dele

from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q # permite usar 'or' nos filtros da pesquisa



# Create your views here.

def index(request):
    contacts = Contact.objects.filter(show=True)\
        .order_by('-id') 
    
    # print(contacts.query) # mostra a query que está sendo executada
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos -'
    }
    
    return render(
        request, 
        'contact/index.html',
        context,
    )


def contact(request, contact_id):
    # podemos usar o get para pegar um id específico, mas caso ele não encontre um valor 
    # ou encontre mais de um valor ele vai lançar um erro
    # single_contact = Contact.objects.get(id=contact_id)
    
    # a maneira mais simples de corrigir o problema do get é usar o filter e pegar o primeiro valor
    # single_contact = Contact.objects.filter(id=contact_id).first()
    
    # if single_contact is None:
    #     raise Http404('Contact not found')
    
    # essas linhas acima são tão comuns que já existe um func no django para fazer isso 
    single_contact = get_object_or_404(
        Contact, 
        id=contact_id,
        show=True,
    )
    
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    
    return render(
        request, 
        'contact/contact.html',
        context,
    )

def search(request):
    # o q é o nome do form lá no _header
    search_value = request.GET.get('q', '').strip() # GET retorna um QueryDict
    
    if search_value == '':
        return redirect('contact:index')
    
    # field lookups - https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookupshttps://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
    contacts = Contact.objects.filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    
    # print(contacts.query) # mostra a query que está sendo executada
    
    context = {
        'contacts': contacts,
        'site_title': 'Search -',
        'search_value': search_value,
    }
    
    return render(
        request, 
        'contact/index.html',
        context,
    )
