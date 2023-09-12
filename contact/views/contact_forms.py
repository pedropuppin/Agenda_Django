from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm
from django.urls import reverse 
from contact.models import Contact

def create(request):
    # pega a entrada do form
    # search = request.POST.get('first_name')
    
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # formulário que foi postado
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        # garante que só vai salvar se o formulário for válido
        if form.is_valid():
            # contact = form.save(commit=False) # atrasa o save do form para fazer alguma ateração 
            # contact.show = False
            # contact.save()
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)
            
        return render(
            request, 
            'contact/create.html',
            context,
        )

    #formulário vazio
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    
    return render(
        request, 
        'contact/create.html',
        context,
    )

def update(request, contact_id):
    # pega a entrada do form
    # search = request.POST.get('first_name')
    
    #seleciona um contato
    contact = get_object_or_404(Contact, id=contact_id, show=True)
    
    form_action = reverse('contact:update', args=(contact_id, ))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        # formulário que foi postado
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        # garante que só vai salvar se o formulário for válido
        if form.is_valid():
            # contact = form.save(commit=False) # atrasa o save do form para fazer alguma ateração 
            # contact.show = False
            # contact.save()
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)
            
        return render(
            request, 
            'contact/create.html',
            context,
        )

    #formulário vazio
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    
    return render(
        request, 
        'contact/create.html',
        context,
    )        
