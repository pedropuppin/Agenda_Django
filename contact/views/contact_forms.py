from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm
from django.urls import reverse 
from contact.models import Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:login')
def create(request):
    # pega a entrada do form
    # search = request.POST.get('first_name')
    
    # manda o tipo de action do formulário para o template
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        # chama o form de forms.py com os dados do template. O primeiro parametro é o data
        # e o segundo é o request 
        form = ContactForm(request.POST, request.FILES) 
        
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
        # else:
        #     print(form.errors)
        
        return render(
            request, 
            'contact/create.html',
            context,
        )

    #formulário vazio (GET)
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    
    return render(
        request, 
        'contact/create.html',
        context,
    )


@login_required(login_url='contact:login')
def update(request, contact_id):
    # pega a entrada do form
    # search = request.POST.get('first_name')
    
    #seleciona um contato
    contact = get_object_or_404(Contact, id=contact_id, show=True)
    
    form_action = reverse('contact:update', args=(contact_id, ))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
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


@login_required(login_url='contact:login')
def delete(request, contact_id):

    contact = get_object_or_404(
        Contact, 
        id=contact_id, 
        show=True
    )
    
    # request.POST é um dict vindo do form delete do HTML. Estamos usando o .get()
    # para lidar com os dados do dict, falando pra pegar o valor de 'confirmation'
    # e se nenhum valor for encontrado retornamos 'no' por default.
    confirmation = request.POST.get('confirmation', 'no')
    # print('confirma', confirmation) // confirma no

    if confirmation == 'yes':
        # print('confirma', confirmation) // confirma yes
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact, # precisa passar o contexto p o template
            'confirmation': confirmation, # passa o valor de confirmation para o template
        }
    )
