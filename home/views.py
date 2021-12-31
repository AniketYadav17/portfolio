from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")

def project(request):
    return render(request, "projects.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        message = request.POST.get('message')

        data = {
                'name': name,
                'email': email,
                'sub': sub,
                'message': message
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['sub'], message, '', ['anikety0000@gmail.com'])

    return render(request, "contact.html")
