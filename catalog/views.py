from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Имя: {name}\nПочта: {email}\nСообщение: {message}')
    return render(request, 'main/contacts.html')
