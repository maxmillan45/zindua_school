from django.shortcuts import render

def home(request):
    return render(request, 'Zindua/home.html')

def about(request):
    return render(request, 'Zindua/about.html')

def contact(request):
    return render(request, 'Zindua/contact.html')

def programmes(request):
    context = {
        'courses': ['Software Engineering', 'Data Science', 'Cybersecurity', 'Product Management'],
        'updated_date': '2023-10-01'
    }
    return render(request, 'Zindua/programmes.html', context)