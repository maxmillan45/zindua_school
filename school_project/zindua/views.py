from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'zindua/home.html', {'page_title': 'Home'})

def about(request):
    return render(request, 'zindua/about.html', {'page_title': 'About'})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Simple success message
        messages.success(request, f'Thank you {name}! We will contact you soon.')
        return redirect('contact')
    
    return render(request, 'zindua/contact.html', {'page_title': 'Contact'})

def programmes(request):
    return render(request, 'zindua/programmes.html', {'page_title': 'Programmes'})