from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = dict()
    if request.method == "POST":
        name    = request.POST['name']
        email   = request.POST['email']
        sub     = request.POST['subject']
        mesg    = request.POST['message']
        data    = models.Contact.objects.create(
                        name        = name,
                        email       = email,
                        subject     = sub,
                        message     = mesg
            )
        data.save()
        success = {'message' : "Your message is send."}
    return render(request, 'contact.html', success)

def portfolio(request):
    return render(request, 'portfolio.html')

def price(request):
    return render(request, 'price.html')

def services(request):
    return render(request, 'services.html')