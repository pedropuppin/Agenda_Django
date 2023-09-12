from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm

def create(request):
    # pega a entrada do form
    # search = request.POST.get('first_name')
    
    if request.method == 'POST':
        # formulário que foi postado
        context = {
            'form': ContactForm(request.POST),
        }
        
        return render(
            request, 
            'contact/create.html',
            context,
        )

    #formulário vazio
    context = {
        'form': ContactForm(),
    }
    
    return render(
        request, 
        'contact/create.html',
        context,
    )
        