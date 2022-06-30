from django import views
from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    views_dict = dict()
    views_dict['feedbacks'] = models.FeedBack.objects.all()
    return render(request, 'index.html', views_dict)

def about(request):
    return render(request, 'about.html')

def contact(request):
    views_dict = dict()
    views_dict['informations'] = models.Informations.objects.all()
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
        views_dict = {'message' : "Your message is send."}
    return render(request, 'contact.html', views_dict)

def portfolio(request):
    return render(request, 'portfolio.html')

def price(request):
    return render(request, 'price.html')

def services(request):
    return render(request, 'services.html')